import cv2


img_bg = cv2.imread("./test/img/wx_jump_screen_5.png", 0)

# img = cv2.GaussianBlur(img_bg, (3, 3), 0)
# canny = cv2.Canny(img, 50, 150)
cv2.circle(img_bg, (500, 500), 50, (255, 255, 0), 2)
cv2.imwrite('./test/img/result_www.jpg', img_bg)
