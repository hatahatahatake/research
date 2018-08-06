#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Webカメラ 画像取得コード　New!7/23
# raspberryPi3 コンパイル用

import cv2
import glob
import os
import sys
import time
from os import getpid
from os import kill
from threading import Timer
from time import sleep

# VideoCaptureのインスタンスを作成する。
# 引数でカメラを選べれる。
# 0は内蔵カメラ、1は入力カメラ
cap = cv2.VideoCapture(0)
<<<<<<< HEAD
cap.set(4, 800)  # Width
cap.set(4, 600)  # Heigh
cap.set(5, 20)   # FPS
=======
#cap.set(4, 700)  # Width
#cap.set(4, 600)  # Heigh
#cap.set(5, 15)   # FPS

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
>>>>>>> 47a3e520e0f25b7bd1b8766f8078ee266baaf3fb

# ディレクトリパス指定 raspberryPi 用ディレクトリ
sys.path.append('/Desktop/research/Picamera/images')

setnumber = "cap_img"
output_path = "./images"
output_name = output_path + '/' + setnumber

# ディレクトリ確認用(うまく行かなかった時用)
import os
print(os.path.exists(output_path))

print('start')

i = 1;
while(cap.isOpened()):
    # VideoCaptureから1フレーム読み込む
    ret, frame = cap.read()

    if ret == True:
        frame = cv2.flip(frame, 180)

        out.write(frame)

<<<<<<< HEAD
    # raspy/image ディレクトリに取得画像を自動保存
    cv2.imwrite(output_name + str(i) + ".png", frame)
    print(setnumber + str(i) + ".png")
    i += 1
=======
        # 動画を取得
        cv2.imshow("FLAME IMAGE", frame)
    
        time.sleep(30)
>>>>>>> 47a3e520e0f25b7bd1b8766f8078ee266baaf3fb

        # raspy/image ディレクトリに取得画像を自動保存
        cv2.imwrite(output_name + str(i) + ".png", frame)
        print(setnumber + str(i) + ".png")
        i += 1

        # キー入力を1ms待って、k が27（ESC）だったらBreakする
        k = cv2.waitKey(1)
        if k == 27:
            break
        
        print('end')
    
    else:
        break

# キャプチャをリリースして、ウィンドウをすべて閉じる
cap.release()
out.release()
cv2.destroyAllWindows()
