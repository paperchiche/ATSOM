# Задание 5. Прочитать изображение, перевести его в формат HSV.
# Вывести на экран два окна, в одном изображение в формате HSV, в другом –
# исходное изображение.

import cv2

image_path = r'C:/Users/20art/Desktop/01.jpg'
img = cv2.imread(image_path)

cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('HSV', cv2.WINDOW_NORMAL)

cv2.imshow("Original", img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("HSV", hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()