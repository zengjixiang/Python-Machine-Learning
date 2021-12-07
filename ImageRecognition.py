import cv2; # OpenCV
import os.path; # Path
import numpy as np; # Numpy
from matplotlib import pyplot as plt; # Matplotlib

# documentation: https://docs.opencv.org/3.4/d4/d86/tutorial_py_histogram_equalization.html

# Author: Ji-Xiang Zeng
# Copyright (c) 2021, All rights reserved.


imagePath = "./images/human.jpg"; # 影像路徑

img = "" # 初始化 image 變數

# 確認影像是否存在
if os.path.isfile(imagePath):
    img = cv2.imread(imagePath)                         # 讀取影像
else:
    print ("The file" + imagePath +" does not exist.")  # 影像不存在
    exit()                                              # 結束程式

# print(type(img))

cv2.imshow('image',img) # 顯示圖檔

# 影像轉灰階
img_RGB_to_grayscale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)    # 將影像轉為灰階 (RGB -> Grayscale)
img_BGR_to_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 將影像轉為灰階 (BGR -> Grayscale)
plt.imshow(img_RGB_to_grayscale)                                # 顯示圖檔
plt.title('img_grayscale')                                      # 圖檔標題
plt.show()                                                      # 顯示圖檔

# to be continued...

cv2.waitKey(0) # 等待按鍵
cv2.destroyAllWindows() # 關閉所有視窗

