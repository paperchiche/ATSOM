# Задание 2. Вывести на экран изображение. Протестировать три
# возможных расширения, три различных флага для создания окна и три
# различных флага для чтения изображения.

# Примеры флагов для создания окна
# 1. cv2.WINDOW_NORMAL - Окно с изменяемым размером
# 2. cv2.WINDOW_AUTOSIZE - Окно с фиксированным размером
# 3. cv2.WINDOW_FULLSCREEN - Полноэкранное окно

# Примеры флагов для чтения изображения
# 1. cv2.IMREAD_COLOR - Чтение изображения в цвете (по умолчанию)
# 2. cv2.IMREAD_GRAYSCALE - Чтение изображения в оттенках серого
# 3. cv2.IMREAD_UNCHANGED - Чтение изображения без изменений

import cv2
image_extensions = ["png", "jpg", "bmp"]
image_path = r'C:/Users/20art/Desktop/02.png'

# Читаем изображение в оттенках серого
image1 = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('Window 1', cv2.WINDOW_FULLSCREEN)
cv2.imshow('Window 1', image1)
cv2.waitKey(0)


image2 = cv2.imread(image_path, cv2.IMREAD_COLOR)
cv2.namedWindow('Window 2', cv2.WINDOW_NORMAL)
cv2.imshow('Window 2', image2)
cv2.waitKey(0)

# Читаем изображение с учетом любой глубины цвета
image3 = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
cv2.namedWindow('Window 3', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Window 3', image3)
cv2.waitKey(0)

# Закрываем все открытые окна
cv2.destroyAllWindows()