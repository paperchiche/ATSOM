# -*- coding: cp1251 -*-
import math
import cv2

def draw_star(image, middle, size, angle_degrees):
    points = []

    for i in range(5):
        x = int(middle[0] + size * math.cos(math.radians(i * 72 + angle_degrees)))
        y = int(middle[1] + size * math.sin(math.radians(i * 72 + angle_degrees)))
        points.append((x, y))

    for i in range(5):
        cv2.line(image, points[i], points[(i + 2) % 5], (0, 0, 0), 4)

    cv2.circle(image, middle, size, (0, 0, 0), 4)

img = cv2.imread(r'C:/Users/20art/Desktop/01.jpg')

# Координаты центра изображения
middle = (img.shape[1] // 2, img.shape[0] // 2)

star_size = 100  # Размер пятиконечной звезды
star_angle = 54

draw_star(img, middle, star_size, star_angle)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
