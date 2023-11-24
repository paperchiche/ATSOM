# -*- coding: cp1251 -*-
import cv2
import numpy as np

# ������ VideoCapture ��� ����������� � IP-������
cap = cv2.VideoCapture(0)

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
        color = (0, 0, 0)  # ������ ����
        thickness = 2  # �������
        cv2.rectangle(frame,
            (c_x - (width // 8), c_y - (height // 8)),
            (c_x + (width // 8), c_y + (height // 8)),
            color, thickness)

    cv2.imshow('HSV_frame', hsv)
    cv2.imshow('Result_frame', frame)


    if cv2.waitKey(1) & 0xFF == 27:
        break

print("������� �������:", area)

cap.release()
cv2.destroyAllWindows()