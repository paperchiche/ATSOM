# -*- coding: cp1251 -*-
import math
import cv2
import numpy as np

def closest_color(x, y):
    colors = {
        "0": (255, 0, 0),   # Red
        "1": (0, 255, 0),   # Green
        "2": (0, 0, 255)    # Blue
    }
    (r, g, b) = img[np.int16(y), np.int16(x)]  # ���������� ����� ������� � ����������� (x, y)
    min_distance = float('inf')  # ��� ���������� ����� ������� ������ ������� � ������� �� �������.
    closest = None
    for color_name, color_value in colors.items():
        distance = sum(((r, g, b) - np.array(color_value)) ** 2)  # ������� ��������� ���������� ����� ������ �������� ������� � ������� �� �������
        if math.sqrt(distance) < min_distance:
            min_distance = math.sqrt(distance)
            closest = color_name

    return closest


img = cv2.imread(r'C:/Users/20art/Desktop/01.jpg')

height, width, _ = img.shape  # ���������� ������ �����������, ������ � ���������� ������� �����
center_x = width // 2         # ���������� ��������� ������
center_y = height // 2

closest = closest_color(center_x, center_y)  # ����������� ���������� ����� � ������������ �������

star_color = (0, 0, 0)  # ����������� ����� �����������
if closest == "0":
    star_color = (255, 0, 0)   # �������
elif closest == "1":
    star_color = (0, 255, 0)   # �������
elif closest == "2":
    star_color = (0, 0, 255)   # �����

print("Color at center pixel is - Red: {}, Green: {}, Blue: {}".format(
    img[np.int16(center_y), np.int16(center_x)][2],
    img[np.int16(center_y), np.int16(center_x)][1],
    img[np.int16(center_y), np.int16(center_x)][0]))


def draw_star(image, size, angle_degrees, color):
    points = []

    for i in range(5):
        x = int(middle[0] + size * math.cos(math.radians(i * 72 + angle_degrees)))
        y = int(middle[1] + size * math.sin(math.radians(i * 72 + angle_degrees)))
        points.append((x, y))

    for i in range(5):
        cv2.line(image, points[i], points[(i + 2) % 5], color, 4)

    cv2.circle(image, middle, size, color, 4)


middle = (img.shape[1] // 2, img.shape[0] // 2)  # ���������� ������ �����������

star_size = 100  # ������ ������������ ������
star_angle = 54

draw_star(img, star_size, star_angle, star_color)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()