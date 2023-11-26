# -*- coding: cp1251 -*-
import random

import cv2
import numpy as np


cap = cv2.VideoCapture(0)
color_1 = 0
color_2 = 0
color_3 = 0
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # ����������� ��������� �������� ����� � HSV
    lower_red = np.array([0, 120, 200]) # ����������� �������� �������, ������������ � ��������(�������)
    upper_red = np.array([100, 255, 255]) # ������������ �������� �������, ������������ � ��������(�������)

    # ����� - �������� �����������, ��� �������, ��������������� ��������� ��������� �����, ����� �������� 255 (�����), � ��������� ������� ����� �������� 0 (������).
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # ���������� ����� �� �����������
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # ���������� ������� �� ������ �����
    moments = cv2.moments(mask)

    # ����� ������� ������� �������
    area = moments['m00']

    if area > 0:
        # ������ � ������ �������������� ����� ����������� ����� �� ������� �������
        width = height = int(np.sqrt(area))
        # ���������� ��������� ������ ������� �� ����������� � �������������� ������ ������� �������
        c_x = int(moments["m10"] / moments["m00"])
        c_y = int(moments["m01"] / moments["m00"])
        # ��������� ��������������
        color = (0, 0, 0) # ������ ����
        color_1 = random.randint(0, 255)
        color_2 = random.randint(0, 255)
        color_3 = random.randint(0, 255)
        thickness = 2 # �������
        print(width)
        c = 5
        cv2.rectangle(frame,

            (c_x - (width // 20), c_y - (height // 20)),
            (c_x + (width // 20), c_y + (height // 20)),
            color, thickness)

        a = 7
        b = 1000
        cv2.rectangle(frame,
                      (c_x - (b // 256) - a, c_y - (b // 256)),
                      (c_x + (b // 256) - a, c_y + (b // 256)),
                      (color_1,color_2,color_3), -1)
        cv2.rectangle(frame,
                      (c_x - (b // 256) + a, c_y - (b // 256)),
                      (c_x + (b // 256) + a, c_y + (b // 256)),
                      (color_1,color_2,color_3), -1)
        cv2.rectangle(frame,
                      (c_x - (b // 256) , c_y - (b // 256) - a),
                      (c_x + (b // 256) , c_y + (b // 256) - a),
                      (color_1,color_2,color_3), -1)
        cv2.rectangle(frame,
                      (c_x - (b // 256), c_y - (b // 256) + a),
                      (c_x + (b // 256), c_y + (b // 256) + a),
                      (color_1,color_2,color_3), -1)


    cv2.imshow('Result_frame', frame)

    if cv2.waitKey(1) & 0xFF == ord(" "):
        break

print("������� �������:", area)


cap.release()
cv2.destroyAllWindows()