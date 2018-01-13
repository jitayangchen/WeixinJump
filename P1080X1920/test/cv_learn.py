import cv2
import numpy as np


img_bg = cv2.imread("./img/wx_jump_screen_551.png", 0)
img_target = cv2.imread("./res/target.jpg", 0)

img = cv2.GaussianBlur(img_bg, (5, 5), 0)
canny = cv2.Canny(img, 1, 20)
# H, W = canny.shape
# y_top = np.nonzero([max(row) for row in canny[400:]])[0][0] + 400
# x_top = int(np.mean(np.nonzero(canny[y_top])))
# y_bottom = y_top + 50
# for row in range(y_bottom, H):
#     if canny[row, x_top] != 0:
#         y_bottom = row
#         break
#
# x_center, y_center = x_top, (y_top + y_bottom) // 2
#
# # cv2.rectangle(canny, (0, y_top), (500, y_top + 10), (255, 255, 0), 2)
# cv2.circle(canny, (x_center, y_center), 10, (255, 255, 0), 2)
cv2.imwrite('./img/contours3.jpg', canny)

# res = cv2.matchTemplate(img_bg, img_target, cv2.TM_CCOEFF_NORMED)
# min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res)
# cv2.rectangle(img_bg, max_loc1, (max_loc1[0] + 77, max_loc1[1] + 209), (0, 255, 0), 3)
# cv2.imwrite('./img/contours.jpg', img_bg)
