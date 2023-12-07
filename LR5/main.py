# -*- coding: cp1251 -*-
import cv2
import numpy as np

i = 0
def main(kernel_size, standard_deviation):
    global i
    i += 1

    # ������ ����� �� �����
    video_source = cv2.VideoCapture('main_video.mov', cv2.CAP_ANY)
    # ���������� ������� �����
    ret, frame = video_source.read()
    # ������� � �����-����� ������
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # ���������� �������� ������
    img = cv2.GaussianBlur(img, (kernel_size, kernel_size), standard_deviation)

    # ���������� ������
    # ����������� ������� ����� ��� ������
    w = int(video_source.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video_source.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # ����������� ������� ����������
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # ������ ����� � ����
    # video_writer = cv2.VideoWriter( 'result_videos/result' + str(i) + '.mp4', fourcc, 25, (w, h))

kernel_size = 3
standard_deviation = 10

main(kernel_size, standard_deviation)