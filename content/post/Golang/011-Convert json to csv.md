---
title: "01-Convert json to csv"
author: "lucas"
date: 2021-06-09
lastmod: 2021-06-09

tags: ["go"]
categories: ["Go"]
keywords: ["go", "json", "csv"]
---

# Table of Contents

- [Table of Contents](#table-of-contents)
- [1: Convert json to csv](#1-convert-json-to-csv)
  - [1.1 json 文件](#11-json-文件)
  - [1.2 convert](#12-convert)

# 1: Convert json to csv

## 1.1 json 文件

- company.json

```json
[
  { "App": "Instagram", "Company": "Facebook", "Category": "Social Media" },
  { "App": "WeChat", "Company": "Tencent", "Category": "Social Media" },
  { "App": "Hotstar", "Company": "Disney", "Category": "Entertainment" },
  { "App": "CNBC", "Company": "Comcast", "Category": "News" },
  { "App": "SnapChat", "Company": "Snap", "Category": "Social Media" }
]
```

## 1.2 convert

```bash
package main

import (
    "encoding/csv"
    "encoding/json"
    "fmt"
    "io/ioutil"
    "os"
)

// Application struct
type Application struct {
    App      string
    Company  string
    Category string
}

func main() {
    // read data from file
    jsonDataFromFile, err := ioutil.ReadFile("./company.json")

    if err != nil {
        fmt.Println(err)
    }

    // Unmarshal JSON data
    var jsonData []Application
    err = json.Unmarshal([]byte(jsonDataFromFile), &jsonData)

    if err != nil {
        fmt.Println(err)
    }

    csvFile, err := os.Create("./data.csv")

    if err != nil {
        fmt.Println(err)
    }
    defer csvFile.Close()

    writer := csv.NewWriter(csvFile)

    for _, usance := range jsonData {
        var row []string
        row = append(row, usance.App)
        row = append(row, usance.Company)
        row = append(row, usance.Category)
        writer.Write(row)
    }

    // remember to flush!
    writer.Flush()
}
```
