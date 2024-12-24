import pysftp
import os
import sys
import time
import gnupg

from etc import config
import utils
from utils import logger_web
from utils import logger_lms as logger


# -----------------------------
broker=config.LMS["broker"]
notifier_list=config.Notifier
notifier_list2=config.Notifier2
# -----------------------------

class SFTPClient:
    def __init__(self, host,port, username, password, upload_dir, download_dir,gpg_key_id='D7B7817A'):
        self.host = host
        self.port = port
        self.username = username 
        self.password = password
        self.upload_dir = upload_dir
        self.download_dir = download_dir
        self.sftp = None
        self.gpg = gnupg.GPG(gnupghome="/root/.gnupg")
        self.gpg_key_id=gpg_key_id
        self.max_retries = 3
        self.retry_delay = 5
        # 禁用主机密钥检查
        self.cnopts = pysftp.CnOpts()
        self.cnopts.hostkeys = None
        self.connect()

    def ensure_connected(self):
        """确保SFTP连接是活跃的，如果断开则重连"""
        try:
            self.sftp.listdir()
        except Exception as e:
            logger.error("SFTPClient connection check failed, error={}".format(e))
            self.connect()
            time.sleep(3)

    def connect(self):
        """建立SFTP连接，包含重试机制"""
        for attempt in range(self.max_retries):
            try:
                if self.sftp:
                    try:
                        self.sftp.close()
                    except Exception as e:
                        logger.error("SFTPClient during disconnect error: {}".format(e))
                self.sftp = pysftp.Connection(
                    host=self.host,
                    port=self.port,
                    username=self.username,
                    password=self.password,
                    cnopts=self.cnopts
                )
                logger.info("SFTPClient connected to {}, connected success ...".format(self.host))
                return True
            except Exception as e:
                logger.error("SFTPClient connection attempt {} failed, error={}".format(attempt+1, e))
                if attempt < self.max_retries-1:
                    logger.error("SFTPClient Retrying in {} seconds...".format(self.retry_delay))
                    time.sleep(self.retry_delay)
        return False

    def upload_file(self, local_path):
        logger.info("SFTPClient start upload file={} to remote_path={}".format(local_path, self.upload_dir))
        if not os.path.exists(local_path):
            logger.error("SFTPClient UploadFile ={} does not exist".format(local_path))
            return False
            
        for attempt in range(self.max_retries):
            try:
                self.ensure_connected()
                self.sftp.chdir(self.upload_dir)
                filename = os.path.basename(local_path)
                self.sftp.put(local_path)
                logger.info("SFTPClient Successfully upload file={} to remote_path={}".format(filename, self.upload_dir))
                self.close()
                utils.send_message('markdown', "{} SFTP upload_file".format(broker), 
                           "## {} SFTP upload_file success\nFtpSide={}\nFtpUser={}\nfile={}\n".format(broker,
                            config.LMS['ftp_url'],config.LMS['ftp_user'],filename),notifier_list)
                local_csvfile=local_path.replace(".pgp",'')
                utils.weichat_send_file(local_csvfile)
                return True
            except Exception as e:
                logger.error("SFTPClient Failed upload file={}, attempt {} error={}".format(local_path, attempt+1, str(e)))
                if attempt < self.max_retries-1:
                    logger.error("SFTPClient Retrying upload file={}, seconds...".format(local_path))
                    time.sleep(self.retry_delay)
        return False

    def search_file(self, filename):
        logger.info("SFTPClient start search remote_path={}/{} ...".format(self.download_dir, filename))
        for attempt in range(self.max_retries):
            try:
                self.ensure_connected()
                self.sftp.chdir(self.download_dir)
                files = self.sftp.listdir()
                logger.info(f"----------listdir-----------------{self.download_dir}---------------------------")
                logger.info(f"-------------------------{filename}---------------------{attempt+1}--------------------")
                logger.info(files)
                logger.info("--------------------------------------------------------------------")
                logger.info("--------------------------------------------------------------------")
                logger.info("--------------------------------------------------------------------")
                if filename in files:
                    logger.info("SFTPClient search remote_path={}/{} ****** find ******".format(self.download_dir, filename))
                    return True
                return False
            except Exception as e:
                logger.error("SFTPClient search failed remote_path={}/{}, attempt {}, error={}".format(
                    self.download_dir, filename, attempt+1, str(e)))
                if attempt < self.max_retries-1:
                    time.sleep(self.retry_delay)
        return False

    def download_file(self, remote_filename, local_file):
        logger.info("SFTPClient start download remote_path={}/{} to {}".format(
            self.download_dir, remote_filename, local_file))
        for attempt in range(self.max_retries):
            try:
                self.ensure_connected()
                self.sftp.chdir(self.download_dir)
                self.sftp.get(remote_filename, local_file)
                logger.info("SFTPClient Successfully downloaded {} to {}".format(remote_filename, local_file))
                self.close()
                utils.send_message('markdown', "{} SFTP download_file".format(broker), 
                           "## {} SFTP download_file success\nFtpSide={}\nFtpUser={}\nfile={}\n".format(broker,
                            config.LMS['ftp_url'],config.LMS['ftp_user'],remote_filename),notifier_list)
                return True
            except Exception as e:
                logger.error("SFTPClient Download failed remote_path={}/{}, attempt {}, error={}".format(
                    self.download_dir, remote_filename, attempt+1, str(e)))
                if attempt < self.max_retries-1:
                    time.sleep(self.retry_delay)
                    if os.path.exists(local_file):
                        try:
                            os.remove(local_file)  # 删除可能的部分下载文件
                        except Exception as e:
                            logger.error("SFTPClient Download failed remote_path={}/{}, remove partial download local_path={}, error={}".format(
                                self.download_dir, remote_filename, local_file, str(e)))
        return False

    def close(self):
        if self.sftp:
            try:
                self.sftp.close()
            except Exception as e:
                logger.error("SFTPClient close has error:{}".format(e))