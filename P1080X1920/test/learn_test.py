import cv2
import numpy as np


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
        canny = cv2.Canny(img, 1, 10)
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


TOP_PADDING = 400

target_img = cv2.imread("./res/target.jpg", 0)
white_circle = cv2.imread('./res/white_circle.jpg', 0)
wx_jump_screen = cv2.imread("./img/wx_jump_screen_33.png", 0)

max_loc_target = get_target_position()
# max_loc_target = (max_loc_target[0] + 39, max_loc_target[1] + 189)

canny_img, next_x, next_y = get_next_position()

cv2.line(canny_img, (max_loc_target[0] + 39, max_loc_target[1] + 189), (next_x, next_y), (255, 255, 0), 2)
cv2.rectangle(canny_img, max_loc_target, (max_loc_target[0] + 78, max_loc_target[1] + 210), (0, 255, 0), 3)
cv2.imwrite('./img/result_' + str(00) + '.jpg', canny_img)
