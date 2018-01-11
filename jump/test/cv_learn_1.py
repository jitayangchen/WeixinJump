import cv2
import numpy as np


TOP_PADDING = 600


wx_jump_screen = cv2.imread("./test/img/wx_jump_screen_0.png", 0)
img_target = cv2.imread("./test/img/white_circle.jpg", 0)
res = cv2.matchTemplate(wx_jump_screen, img_target, cv2.TM_CCOEFF_NORMED)
min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res)
# (-0.49441006779670715, 0.5061903595924377, (332, 909), (504, 557))
print(min_val1)
print(max_val1)
print(min_loc1)
print(max_loc1)
cv2.rectangle(wx_jump_screen, max_loc1, (max_loc1[0] + 53, max_loc1[1] + 32), (0, 255, 0), 3)
cv2.imwrite('./test/img/contours_1.jpg', wx_jump_screen)


# def get_next_position():
#
#     img = cv2.GaussianBlur(wx_jump_screen, (3, 3), 0)
#     canny = cv2.Canny(img, 50, 150)
#     h, w = canny.shape
#
#     # for m in range(max_loc_target[1] - 10, max_loc_target[1] + 285):
#     #     for n in range(max_loc_target[0] - 10, max_loc_target[0] + 105):
#     #         canny[m][n] = 0
#
#     y_top = np.nonzero([max(row) for row in canny[TOP_PADDING:]])[0][0] + TOP_PADDING
#     x_top = int(np.mean(np.nonzero(canny[y_top])))
#     y_bottom = y_top + 100
#     for row in range(y_bottom, h):
#         if canny[row, x_top] != 0:
#             y_bottom = row
#             break
#
#     x_center, y_center = x_top, (y_top + y_bottom) // 2
#     return canny, x_center, y_center
#
#
# canny_img, next_x, next_y = get_next_position()
#
# cv2.circle(canny_img, (next_x, next_y), 20, (255, 255, 0), 2)
# cv2.imwrite('./test/img/contours.jpg', canny_img)
