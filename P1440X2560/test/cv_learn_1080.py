import cv2
import os

img_bg = cv2.imread("./img/wx_jump_screen1080.png", 1)
# 1440 2560
# game_over.png
# cv2.imwrite('./img/contours1080.jpg', img_bg[1505:1662, 284:796])

# target.jpg
# cv2.imwrite('./img/contours1080.jpg', img_bg[911:1121, 314:392])

# 圆点
cv2.imwrite('./img/contours1080.jpg', img_bg[819:843, 793:833])

# Test
# cv2.imwrite('./img/contours1080.jpg', img_bg[0:600, 0:1440])

# arr = [1, 3, 2, 3, 5, 7, 0]
# print(arr)
# print(arr[2:])

# os.system('adb shell screencap -p /sdcard/wx_jump_screen1080.png')
# os.system('adb pull /sdcard/wx_jump_screen1080.png ./img')
