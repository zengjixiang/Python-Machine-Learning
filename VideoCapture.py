import cv2; # OpenCV
import numpy as np; # Numpy
from matplotlib import pyplot as plt; # Matplotlib

# 選擇第一隻攝影機
cap = cv2.VideoCapture(0) 

ret,frame = cap.read() # 讀取影像

if ret == True:
    cv2.imshow('frame',frame) # 顯示圖檔
else:
    print("取消擷取畫面")

cv2.waitKey(0) # 等待按鍵
cv2.destroyAllWindows() # 關閉所有視窗

