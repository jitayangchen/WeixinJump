import cv2


img_bg = cv2.imread("./img/wx_jump_screen_5.png", 0)

img = cv2.GaussianBlur(img_bg, (3, 3), 0)
canny = cv2.Canny(img, 1, 10)
cv2.circle(img_bg, (500, 500), 50, (255, 255, 0), 2)
cv2.imwrite('./img/result_www.jpg', canny)
