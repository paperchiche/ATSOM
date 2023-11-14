# -*- coding: cp1251 -*-
import cv2
import numpy as np

# ������ VideoCapture ��� ����������� � IP-������
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # ����������� ��������� �������� ����� � HSV
    lower_red = np.array([0, 100, 0])
    upper_red = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    moments = cv2.moments(mask)

    area = moments['m00']

    cv2.imshow('HSV_frame', hsv)

    # ������� ������� esc ��� ������ �� �����
    if cv2.waitKey(1) & 0xFF == 27:
        break

print("������� �������:", area)

cap.release()
cv2.destroyAllWindows()