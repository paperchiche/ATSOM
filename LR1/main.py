import cv2
# read image
image = cv2.imread(r'C:/Users/20art/Desktop/01.jpg', cv2.IMREAD_COLOR)
image2 = cv2.imread(r'C:/Users/20art/Desktop/01.jpg', cv2.IMREAD_LOAD_GDAL)
image3 = cv2.imread(r'C:/Users/20art/Desktop/01.jpg', cv2.IMREAD_GRAYSCALE)
# show image
cv2.namedWindow('Display Window', cv2.WINDOW_NORMAL)
cv2.imshow("Display Window", image)
cv2.namedWindow('Display', cv2.WINDOW_AUTOSIZE)
cv2.imshow("Display", image2)
cv2.namedWindow('Display1', cv2.WINDOW_FULLSCREEN)
cv2.imshow("Display1", image3)
flags = cv2.IMREAD_COLOR
# exit at closing of window

cv2.waitKey(0)
cv2.destroyAllWindows()