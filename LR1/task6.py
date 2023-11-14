# Задание 6 (самостоятельно) Прочитать изображение с камеры. Вывести
# в центре на экране Красный крест в формате, как на изображении. Указать
# команды, которые позволяют это сделать.

import cv2

img = cv2.imread(r'C:/Users/20art/Desktop/01.jpg')
height, width, _ = img.shape

# Расчет координат центра изображения
center_x = width // 2
center_y = height // 2

# Размер и цвет прицела
crosshair_size = 70
crosshair_color = (255, 255, 255)  # Белый цвет прицела

# Отрисовка вертикальной линии прицела
cv2.line(img, (center_x, center_y - crosshair_size // 2), (center_x, center_y + crosshair_size // 2), crosshair_color, 2)

# Отрисовка горизонтальной линии прицела
cv2.line(img, (center_x - crosshair_size // 2, center_y), (center_x + crosshair_size // 2, center_y), crosshair_color, 2)

# Радиус и цвет круга внутри прицела
circle_radius = 5
circle_color = (0, 0, 255)  # Красный цвет внутри

# Отрисовка круга внутри прицела
cv2.circle(img, (center_x, center_y), circle_radius, circle_color)

# Отображение изображения с прицелом
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.namedWindow('image', cv2.WINDOW_NORMAL)  # Окно с изменяемым размером
cv2.imshow('image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()