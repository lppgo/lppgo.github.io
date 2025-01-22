---
title: "017-pysftp SFTP Pool"
author: "lucas"
description: "017-pysftp SFTP Pool "
date: 2024-12-18
lastmod: 2025-01-22

categories: ["Python"]
tags: ["Python", "pysftp", "SFTP"]
keywords: ["Python", "pysftp", "SFTP"]
---

# pysftp SFTP Pool

```python3

import pysftp
import os
import sys
import time
import paramiko
from queue import Queue, Empty

# -----------------------------


from etc import config
import utils
from utils import logger_web
from utils import logger_lms as logger


# -----------------------------
broker=config.LMS["broker"]
notifier_list=config.Notifier
notifier_list2=config.Notifier2

# -----------------------------

class SFTPConnectionPool:
    """SFTP连接池"""
    def __init__(self,host,port,username,password,max_connections=20):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.max_connections = max_connections
        self.pool=Queue(maxsize=max_connections)
        self.cnopts = paramiko.SSHClient()
        self.cnopts.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # self.cnopts.hostkeys = None
        self._init_pool()

    def _init_pool(self):
        for _ in range(self.max_connections):
            conn=self._create_conn()
            if conn:
                self.pool.put(conn)
            else:
                logger.error("初始化SFTP连接池失败")

    def _create_conn(self):
        transport=paramiko.Transport((self.host,self.port))
        transport.connect(username=self.username,password=self.password)
        return paramiko.SFTPClient.from_transport(transport)

    def get_conn(self):
        try:
            return self.pool.get(timeout=10)
        except Empty:
            logger.error("SFTPConnPool no avaiable connections ...")

    def release_conn(self,conn):
        if conn:
            self.pool.put(conn) # 将对象放回连接池
        else:
            logger.warning("SFTPConnPool attempted to release a None connection")

    def close_all_conn(self):
        while not self.pool.empty():
            conn=self.pool.get()
            if conn:
                conn.close()
            else:
                logger.warning("SFTPConnPool Found a None connection in the pool")




class SFTPClient:
    def __init__(self, host,port, username, password, upload_dir, download_dir):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.upload_dir = upload_dir
        self.download_dir = download_dir
        self.max_retries = 3
        self.retry_delay = 5
        self.pool=SFTPConnectionPool(host,port,username,password)

    def ensure_connected(self):
        """确保SFTP连接是活跃的，如果断开则重连"""
        sftp=self.pool.get_conn()
        if not sftp:
            return False
        try:
            sftp.listdir()
            return True
        except Exception as e:
            logger.error("SFTPClient connection check failed, error={}".format(e))
            self.pool.release_conn(sftp)
            time.sleep(3)
            return False

    def upload_file(self, local_file):
        logger.info(f"SFTPClient start upload file={local_file} to remote_path={self.upload_dir}")
        if not os.path.exists(local_file):
            logger.error("SFTPClient UploadFile ={} does not exist".format(local_file))
            return False
        for attempt in range(self.max_retries):
            try:
                if not self.ensure_connected():
                    continue
                sftp=self.pool.get_conn()
                sftp.chdir(self.upload_dir)
                filename = os.path.basename(local_file)
                sftp.put(local_file) # /root/project/lms_jpm/static/files/xxx_request.csv
                logger.info(f"SFTPClient Successfully upload file={filename} to remote_path={self.upload_dir}")
                return True
            except Exception as e:
                logger.error(f"SFTPClient Failed upload file={local_file}, attempt {attempt+1} error={e}")
                if attempt < self.max_retries-1:
                    logger.error(f"SFTPClient Retrying upload file={local_file}, seconds ...")
                    time.sleep(self.retry_delay)
        return False

    def search_file(self, file):
        logger.info(f"SFTPClient start search remote_path={self.download_dir}/{file} ...")
        for attempt in range(self.max_retries):
            try:
                self.ensure_connected()
                self.conn.chdir(self.download_dir)
                files = self.conn.listdir()
                # logger.info(f"----------listdir-----------------{self.download_dir}---------------------------")
                # logger.info(f"-------------------------{file}---------------------{attempt+1}--------------------")
                # logger.info(files)
                # logger.info("--------------------------------------------------------------------")
                # logger.info("--------------------------------------------------------------------")
                # logger.info("--------------------------------------------------------------------")
                if file in files:
                    # logger.info(f"SFTPClient search remote_path={self.download_dir}/{file} ****** find ******")
                    return True
                return False
            except Exception as e:
                logger.error(f"SFTPClient search failed remote_path={self.download_dir}/{file}"+
                    f", attempt= {attempt+1}, error={e}")
                if attempt < self.max_retries-1:
                    time.sleep(self.retry_delay)
        return False

    def download_file(self, file, local_path):
        logger.info(f"SFTPClient start download remote_file={file} to {local_path}")
        for attempt in range(self.max_retries):
            try:
                if not self.ensure_connected():
                    continue
                sftp=self.pool.get_conn()
                sftp.chdir(self.download_dir)
                sftp.get(file, local_path)
                logger.info(f"SFTPClient Successfully downloaded {file} to {local_path}")
                return True
            except Exception as e:
                logger.error(f"SFTPClient Download failed remote_file={file}, attempt= {attempt+1}, error={e}")
                if attempt < self.max_retries-1:
                    time.sleep(self.retry_delay)
                    if os.path.exists(f"{local_path}/{file}"):
                        os.remove(f"{local_path}/{file}")  # 删除可能的部分下载文件
        return False

```
