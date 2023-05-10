
<div align="center"><font size="35">go将html转为image图片</font></div>

# 1: 概述

- 将 html 转为 image 图片
- 用于从 HTML/CSS 生成高质量图像的 API
- https://docs.htmlcsstoimage.com/

# 2: go 代码

```go
package pkgs

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"time"
)

// 用于从 HTML/CSS 生成高质量图像的 API
// https://docs.htmlcsstoimage.com/
const (
	userID = "c721cbd9-9ddf-4efb-b97c-0616490d98ac"
	apiKey = "aa7c90f4-b2ef-4a6c-85af-e24141c10750"
)

func My_Image() {
	data := map[string]string{
		// "html": `"<div class='ping'>Pong ✅</div>"`,
		"device_scale": "1",
		"html": fmt.Sprintf(`
<div style="height: 455px; width: 1068px;  ">
    <style>
        .line {
            background-color: #f2f2f2;
        }
    </style>
    <table border: 1px solid;>
        <tr class='title' bgcolor='#008888'>
            <th style="width: 100px;">Host</th>
            <th style="width: 150px;">Account</th>
            <th style="width: 50px;">StatusCode</th>
            <th style="width: 100px;">Status</th>
            <th style="width: 666px;">ErrMsg</th>
        </tr>
        <tr class='line' >
            <td>192.168.8.1</td>
            <td>mshw_ms03</td>
            <td>1</td>
            <td>PENDING_CANCEL</td>
            <td>INVALID_BOC_TYPE_BY_CLIENT</td>
        </tr>
        <tr class='line'>
            <td>192.168.8.3</td>
            <td>mshw_baml18</td>
            <td>2</td>
            <td>REJECTED</td>
            <td>99 : 2043 Invalid order price!</td>
        </tr>
        <tr class='line' >
            <td>192.168.8.3</td>
            <td>mshw_baml18</td>
            <td>3</td>
            <td>REJECTED</td>
            <td>99 : 2043 Invalid order price!</td>
        </tr>
        <tr class='line' >
            <td>192.168.8.3</td>
            <td>mshw_baml18</td>
            <td>4</td>
            <td>REJECTED</td>
            <td>99 : 2043 Invalid order price!</td>
        </tr>
        <tr class='line' >
            <td>192.168.8.3</td>
            <td>mshw_baml18</td>
            <td>5</td>
            <td>REJECTED</td>
            <td>99 : 2043 Invalid order price!</td>
        </tr>
        <tr class='line' >
            <td>192.168.8.3</td>
            <td>mshw_baml18</td>
            <td>6</td>
            <td>REJECTED</td>
            <td>99 : 2043 Invalid order price!</td>
        </tr>
        <tr class='line' >
            <td>192.168.8.3</td>
            <td>mshw_baml18</td>
            <td>1</td>
            <td>REJECTED</td>
            <td>99 : 2043 Invalid order price!</td>
        </tr>
        <tr class='line' >
            <td>192.168.8.3</td>
            <td>mshw_baml18</td>
            <td>2</td>
            <td>REJECTED</td>
            <td>99 : 2043 Invalid order price!</td>
        </tr>
    </table>
</div>`),
	}

	reqBody, err := json.Marshal(data)
	if err != nil {
		log.Fatalf("unable to marshal data: %s", err.Error())
	}
	req, err := http.NewRequest("POST", "https://hcti.io/v1/image", bytes.NewReader(reqBody))
	if err != nil {
		log.Fatalf("unable to create new request: %s", err.Error())
	}
	req.SetBasicAuth(userID, apiKey)
	client := &http.Client{Timeout: time.Second * 10}
	resp, err := client.Do(req)
	if err != nil {
		log.Fatalf("request was unsuccessful: %s", err.Error())
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalf("unable to read response body: %s", err.Error())
	}
	fmt.Println(string(body)) // 在线online图片的连接
}

```
