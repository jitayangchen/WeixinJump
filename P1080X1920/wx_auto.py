import os
import random
import cv2
import numpy as np
import time


TOP_PADDING = 400
DEBUG = True


def get_target_position():
    res = cv2.matchTemplate(wx_jump_screen, target_img, cv2.TM_CCOEFF_NORMED)
    min_val1, max_val1, min_loc_target, max_loc_target = cv2.minMaxLoc(res)
    return max_loc_target


def get_next_position():
    res2 = cv2.matchTemplate(wx_jump_screen, white_circle, cv2.TM_CCOEFF_NORMED)
    min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(res2)
    white_circle_h, white_circle_w = white_circle.shape
    if max_val2 > 0.9:
        print('found white circle!')
        x_center, y_center = max_loc2[0] + white_circle_w // 2, max_loc2[1] + white_circle_h // 2
        return wx_jump_screen, x_center, y_center

    else:
        img = cv2.GaussianBlur(wx_jump_screen, (5, 5), 0)
        canny = cv2.Canny(img, 1, 20)
        h, w = canny.shape

        for m in range(max_loc_target[1] - 10, max_loc_target[1] + 215):
            for n in range(max_loc_target[0] - 10, max_loc_target[0] + 80):
                canny[m][n] = 0

        y_top = np.nonzero([max(row) for row in canny[TOP_PADDING:]])[0][0] + TOP_PADDING
        x_top = int(np.mean(np.nonzero(canny[y_top])))
        y_bottom = y_top + 50
        for row in range(y_bottom, h):
            if canny[row, x_top] != 0:
                y_bottom = row
                break

        x_center, y_center = x_top, (y_top + y_bottom) // 2
        return canny, x_center, y_center


def jump(distance):
    press_time = int(distance * 1.35)

    rand = random.randint(0, 9) * 10
    cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) % (320 + rand, 410 + rand, 320 + rand, 410 + rand)
    os.system(cmd)
    print(cmd)


def get_screen_shot(index):
    os.system('adb shell screencap -p /sdcard/wx_jump_screen_%s.png' % index)
    os.system('adb pull /sdcard/wx_jump_screen_%s.png ./img' % index)


if __name__ == "__main__":
    jump(530)
    time.sleep(1)

    if DEBUG:
        for file in os.listdir('./img'):
            os.remove('./img/' + file)

    target_img = cv2.imread("./res/target.jpg", 0)
    game_over_img = cv2.imread('./res/game_over.jpg', 0)
    white_circle = cv2.imread('./res/white_circle.jpg', 0)

    for i in range(10000):
        if DEBUG:
            temp = i
        else:
            temp = 'temp'
        get_screen_shot(temp)

        wx_jump_screen = cv2.imread("./img/wx_jump_screen_%s.png" % temp, 0)
        res_end = cv2.matchTemplate(wx_jump_screen, game_over_img, cv2.TM_CCOEFF_NORMED)
        if cv2.minMaxLoc(res_end)[1] > 0.95:
            print('Game over!')

            # os.system('adb shell input tap 500 1580')
            # time.sleep(1)
            # jump(530)
            # time.sleep(1)
            # continue
            break

        max_loc_target = get_target_position()
        target_bottom_center = (max_loc_target[0] + 39, max_loc_target[1] + 189)

        canny_img, next_x, next_y = get_next_position()

        if DEBUG:
            cv2.line(canny_img, (target_bottom_center[0], target_bottom_center[1]), (next_x, next_y), (255, 255, 0), 2)
            cv2.imwrite('./img/result_' + str(i) + '.jpg', canny_img)

            delete_index = i - 3
            if delete_index >= 0:
                os.remove('./img/wx_jump_screen_%s.png' % delete_index)
                os.remove('./img/result_' + str(delete_index) + '.jpg')

        distance = (abs(target_bottom_center[0] - next_x) ** 2 + abs(target_bottom_center[1] - next_y) ** 2) ** 0.5
        jump(distance)
        time.sleep(1.3)
