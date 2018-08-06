#!usr/bin/python3
# -*- coding: utf-8 -*-

# Webカメラ 画像取得コード　New!8/2

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
#cap.set(4, 700)  # Width
#cap.set(4, 600)  # Heigh
#cap.set(5, 20)   # FPS

fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = int(cap.get(cv2.CAP_PROP_FPS))
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

if (cap.isOpened()== False):
    print("Error opening video stream or file")

# ディレクトリパス指定
sys.path.append('Desktop/iMac-Desktop/git/research_test/raspy/images')

setnumber = "cap_img"
output_path = "./images"
output_name = output_path + '/' + setnumber

# ディレクトリ確認用(うまく行かなかった時用)
import os
print(os.path.exists(output_path))

print('start')

i = 1;
while (cap.isOpened()):
    # VideoCaptureから1フレーム読み込む
    ret, frame = cap.read()

    if ret==True:
        frame = cv2.flip(frame,180)
        out.write(frame)

        # 動画を取得
        cv2.imshow('Frame',frame)

        # sleep を使う方法
        time.sleep(15)

        # raspy/image ディレクトリに取得画像を自動保存
        cv2.imwrite(output_name + str(i) + ".png", frame)
        print(setnumber + str(i) + ".png")
        i += 1

        k = cv2.waitKey(1)
        if k == 27:
            break

    else:
        break

print('end')

# キャプチャをリリースして、ウィンドウをすべて閉じる
cap.release()
#out.release()
cv2.destroyAllWindows()
