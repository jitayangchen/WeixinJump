import cv2
import numpy as np


img_bg = cv2.imread("./test/img/wx_jump_screen_0.jpg", 0)
img_target = cv2.imread("./test/img/target_1.jpg", 0)

img = cv2.GaussianBlur(img_bg, (3, 3), 0)
canny = cv2.Canny(img, 50, 150)
H, W = canny.shape
y_top = np.nonzero([max(row) for row in canny[400:]])[0][0] + 400
x_top = int(np.mean(np.nonzero(canny[y_top])))
y_bottom = y_top + 50
for row in range(y_bottom, H):
    if canny[row, x_top] != 0:
        y_bottom = row
        break

x_center, y_center = x_top, (y_top + y_bottom) // 2

# cv2.rectangle(canny, (0, y_top), (500, y_top + 10), (255, 255, 0), 2)
cv2.circle(canny, (x_center, y_center), 10, (255, 255, 0), 2)
cv2.imwrite('./test/img/contours.jpg', canny)
print(y_top)
# print(canny[0][0])

# cv2.imshow('Canny', canny)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# res = cv2.matchTemplate(img_bg, img_target, cv2.TM_CCOEFF_NORMED)
# min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res)
# (-0.49441006779670715, 0.5061903595924377, (332, 909), (504, 557))
# print(min_val1)
# print(max_val1)
# print(min_loc1)
# print(max_loc1)
# cv2.rectangle(img_bg, max_loc1, (max_loc1[0] + 77, max_loc1[1] + 209), (0, 255, 0), 3)
# cv2.imwrite('./img/contours.jpg', img_bg)
