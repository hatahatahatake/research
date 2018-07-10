# Webカメラ 画像取得コード　New!7/10
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
cap.set(4, 700)  # Width
cap.set(4, 600)  # Heigh
cap.set(5, 15)   # FPS

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
while True:
    # VideoCaptureから1フレーム読み込む
    ret, frame = cap.read()

    # sleep を使う方法
    time.sleep(30)

    # 動画を取得
    cv2.imshow('Raw Frame', frame)

    # raspy/image ディレクトリに取得画像を自動保存
    cv2.imwrite(output_name + str(i) + ".png", frame)
    i += 1

    # キー入力を1ms待って、k が27（ESC）だったらBreakする
    k = cv2.waitKey(1)
    if k == 27:
        break
        print('end')

# キャプチャをリリースして、ウィンドウをすべて閉じる
cap.release()
cv2.destroyAllWindows()
