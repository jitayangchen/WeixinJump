import random

import time
from PIL import Image
import numpy
import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


need_update = False


def get_screen_image():
    os.system('adb shell screencap -p /sdcard/wx_jump_screen_temp.png')
    os.system('adb pull /sdcard/wx_jump_screen_temp.png ./img')

    return numpy.array(Image.open('./img/wx_jump_screen_temp.png'))


def jump_to_next(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = (abs(x2 - x1)**2 + abs(y2 - y1)**2)**0.5
    # os.system('adb shell input swipe 320, 410, 320, 410 {}'.format(int(distance*1.35)))

    press_time = int(distance * 1.35)
    rand = random.randint(0, 9) * 10
    cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) % (320 + rand, 410 + rand, 320 + rand, 410 + rand)
    os.system(cmd)


def on_callback(event, coor=[]):
    global need_update
    coor.append((event.xdata, event.ydata))
    if len(coor) == 2:
        jump_to_next(coor.pop(), coor.pop())
        need_update = True
    # print('you pressed', event.button, event.xdata, event.ydata)
    pass


def update_screen(frame):
    global need_update
    if need_update:
        time.sleep(1)
        axes_image.set_array(get_screen_image())
        need_update = False
    return axes_image,

figure = plt.figure()
axes_image = plt.imshow(get_screen_image(), animated=True)
figure.canvas.mpl_connect('button_press_event', on_callback)
lala = FuncAnimation(figure, update_screen, interval=50, blit=True)
plt.show()
