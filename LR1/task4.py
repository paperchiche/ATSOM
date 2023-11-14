# -*- coding: cp1251 -*-
import cv2

# ��������� ��� �������� �����
input_file = r"C:\GitHub\ATSOM\LR1\video01.mp4"

# ��������� ��� ��������� �����
output_file = "output_video.avi"
frame_width = 1280  # ������ �����
frame_height = 720  # ������ �����
fps = 30  # ���������� ������ � �������

# ��������� ������� �����
cap = cv2.VideoCapture(input_file)

# ���������, ������� �� ������� �����
if not cap.isOpened():
    print("������ ��� �������� �����.")
    exit()

# �������� ������� ����� �� �������� �����
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# ���������� ����� � ������� ������ VideoWriter ��� ������ ��������� �����
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

# ������ ����� �� �������� ����� � ���������� �� � �������� �����
while True:
    ret, frame = cap.read()

    # ���������, ������� �� ������ ����
    if not ret:
        print("������ ��� ������� �����.")
        break

    # ���������� ���� � �������� �����
    out.write(frame)

    # ���������� ����
    cv2.imshow("Video", frame)

    # ����� �� ������� ������� 'q' � ��������� 25 �����������
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# ����������� �������
cap.release()
out.release()
cv2.destroyAllWindows()
