仓库: http://127.0.0.1/ms-tech/ms-offshore

pwd: /root/trade/ems/baml


etc: 
- dataCfg.json

-

dataCfg.json
```json5
{
  // 算法字段-fix tag
  // remark? - MaxVolume
  "TagDict": {"MaxVolume":6403,"MinVolume":6469,"Urgency":6408,"Scaling":6962,"TAGAlgo":6401,"INSTINCT":6401,"Benchmark":8228},
  // account 字段 FixTag1-Account 《香港账户表》
  "fixAcctMap": {"mshw_baml18":"OPTIMA","mshw_baml26":"OPTX","mshw_baml21":"BOOTHBAY","mshw_baml27":"BBFL","mshw_baml27_02":"BBFL2"},
  "fixLogPath": "./log/fix",
  // 函数
  "condParams": [{"func": "!=", "field": "Algorithm", "comparedField":"DMA","tag": 57, "value": "ALGO"},
                {"func": "=", "field": "Algorithm", "comparedField":"DMA","tag": 57, "value": "DMA"}],
  // 强制设置tag 775=1
  "requiredParams": {"775": "1"},
  // tag映射
  "tagMap": {"6401": {"TAGAlgo":"55","INSTINCT":"46"}},
  "targetCompID": "BAML",
  "SenderCompID": "MINGSHICNSWP2",
  "dbPath": "./db",
  // 过滤告警信息
  "excludedErrs":["GLM",
                  "Electronic Short sell Order Reject Alert. Inventory no longer available.",
                 "Market is closed",
                 "Reason: Restricted Name",
                 "Order rejected by short sell",
                 "Order posting at ul/ll is not allowed"]
}


```
tradeCfg.json
```json5
{
        "broker":"BAML",
        "kdb_host": "47.242.173.86",
        "kdb_host-": "47.56.205.31",
        "kdb_port": 5000,
        "auth": "test:pass",
        "accounts": ["mshw_baml18","mshw_baml26","mshw_baml21","mshw_baml27","mshw_baml27_02"],
        "fixFilePath": "./etc/fix.ini",
        "maxNo": 300000,
        "dataCfgPath": "./etc/dataCfg.json"
}

```

// 新配置账户流程
- 《香港账户表》添加记录
- tradeCfg.json 配置账户
- dataCfg.json 配置fix tag1 等信息
