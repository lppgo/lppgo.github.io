---
title: "01-python好用的脚本"
author: "lucas"
description: "..."
date: 2022-09-01
lastmod: 2021-09-01

tags: ["Python", "脚本"]
categories: ["Python"]
keywords: ["python", "脚本"]
---

# 1：图片处理

## 1.1 截图

```python
#! /usr/bin/env python3
# encoding=utf-8


from mss import mss

import PIL.ImageGrab


def screenshot_1():
    """python 截屏方法1
    mss
    """
    with mss() as screenshot:
        screenshot.shot(output="scr.png")


def screenshot_2():
    """python 截屏方法2
    pillow
    """
    scr = PIL.ImageGrab.grab()
    scr.save("scr.png")


def main():
    print("this is main function")
    # screenshot_1()
    screenshot_2()


if __name__ == "__main__":
    main()
    print('__name__ value:', __name__)

```

## 1.2 将图像转换为素描图

```python
# 图像转换
import cv2
# 读取图片
img = cv2.imread("img.jpg")
# 灰度
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey)
# 高斯滤波
blur_img = cv2.GaussianBlur(invert, (7, 7), 0)
inverse_blur = cv2.bitwise_not(blur_img)
sketch_img = cv2.divide(grey, inverse_blur, scale=256.0)
# 保存
cv2.imwrite('sketch.jpg', sketch_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

# 2:

# 3:

# 4:

# 5:

# 6:

# 7:

# 8:

# 9:
