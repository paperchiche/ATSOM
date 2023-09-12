# Задание 6 (самостоятельно) Прочитать изображение с камеры. Вывести
# в центре на экране Красный крест в формате, как на изображении. Указать
# команды, которые позволяют это сделать.

import cv2

img = cv2.imread(r'C:/Users/20art/Desktop/01.jpg')
height, width, _ = img.shape


rect_width = 50  # Ширина прямоугольника
rect_height = 250  # Высота прямоугольника


top_left_x = (width - rect_width) // 2  # Положение вертикали
top_left_y = (height - rect_height) // 2
bottom_right_x = top_left_x + rect_width
bottom_right_y = top_left_y + rect_height
cv2.rectangle(img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 0, 255), 3)  # - ., .,  цвет, толщина

rect_width = 250  # Ширина прямоугольника
rect_height = 50  # Высота прямоугольника

top_left_x = (width - rect_width) // 2  # Положение горизонтали
top_left_y = (height - rect_height) // 2
bottom_right_x = top_left_x + rect_width
bottom_right_y = top_left_y + rect_height
cv2.rectangle(img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 0, 255), 3)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)  # Окно с изменяемым размером
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()