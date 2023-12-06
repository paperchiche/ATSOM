# -*- coding: cp1251 -*-
import cv2
import numpy as np


# ������
def Convolution(img, kernel):
    kernel_size = len(kernel)
    x_start = kernel_size // 2
    y_start = kernel_size // 2
    # ��������������� ������� ����������� ��� ������ � ������ ���������� ��������
    matr = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            matr[i][j] = img[i][j]
    for i in range(x_start, len(matr)-x_start):
        for j in range(y_start, len(matr[i])-y_start):
            #  ������ ������� ���������� �� ��������������� ������� ���� �������, � ����� ��� ������������ �����������
            val = 0
            for k in range(-(kernel_size//2), kernel_size//2+1):
                for l in range(-(kernel_size//2), kernel_size//2+1):
                    val += img[i + k][j + l] * kernel[k + (kernel_size//2)][l + (kernel_size//2)]
            matr[i][j] = val
    return matr


# ���������� ���������� ���� ����� �������� ��������� � ���� �
def get_angle_number(x, y):
    tg = y/x if x != 0 else 999
    if x < 0:
        if y < 0:
            if tg > 2.414:
                return 0
            elif tg < 0.414:
                return 6
            elif tg <= 2.414:
                return 7
        else:
            if tg < -2.414:
                return 4
            elif tg < -0.414:
                return 5
            elif tg >= -0.414:
                return 6
    else:
        if y < 0:
            if tg < -2.414:
                return 0
            elif tg < -0.414:
                return 1
            elif tg >= -0.414:
                return 2
        else:
            if tg < 0.414:
                return 2
            elif tg < 2.414:
                return 3
            elif tg >= 2.414:
                return 4


i = 0


def main(path, standard_deviation, kernel_size, bound_path):
    global i
    i += 1

    # �������� ������
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (500, 500))
    cv2.imshow("Original", img)
    imgBlur_CV2 = cv2.GaussianBlur(img, (kernel_size, kernel_size), standard_deviation)
    cv2.imshow('Blur_Imagine', imgBlur_CV2)

    Gx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    Gy = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

    # ���������� �������� ������
    img_Gx = Convolution(img, Gx)
    img_Gy = Convolution(img, Gy)

    # ��������������� ������� ����������� ��� ������ � ������ ���������� ��������
    matr_gradient = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            matr_gradient[i][j] = img[i][j]

    # ���������� ������� ����� ������� ���������
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            matr_gradient[i][j] = np.sqrt(img_Gx[i][j] ** 2 + img_Gy[i][j] ** 2)

    s = 0

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            s += matr_gradient[i][j]

    for i in range(matr_gradient.shape[0]):
        for j in range(matr_gradient.shape[1]):
            matr_gradient[i][j] /= s

    # ���������� ������� �������� ����� ���������
    img_angles = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_angles[i][j] = get_angle_number(img_Gx[i][j], img_Gy[i][j])

    # ����� ������� �������� ���� ���������
    img_gradient_to_print = matr_gradient.copy()
    # ����� ������������� �������� ����� ���������
    max_gradient = np.max(matr_gradient)
    print(max_gradient)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_gradient_to_print[i][j] = (float(matr_gradient[i][j]) / max_gradient)

    sigma = 2.0
    normalized_matrix_gradient_gaussian = np.exp(-(img_gradient_to_print) ** 2 / (2 * sigma ** 2))

    # normalized_matrix_gradient = img_gradient_to_print / 255.0
    print('������� �������� ���� ���������:')
    # print(normalized_matrix_gradient)
    print(normalized_matrix_gradient_gaussian)

    # ����� ������� �������� ����� ���������
    img_angles_to_print = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_angles_to_print[i][j] = img_angles[i][j] / 7 * 255
    normalized_matrix_angles_gaussian = np.exp(-(img_angles_to_print) / 255) ** 2 / (2 * sigma ** 2)
    print('������� �������� ����� ���������:')
    print(normalized_matrix_angles_gaussian)

    # cv2.imshow('d', normalized_matrix_gradient_gaussian)

    img_border = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            angle = img_angles[i][j]
            gradient = matr_gradient[i][j]
            # �������� ��������� �� ������� �� ������� �����������
            if i == 0 or i == img.shape[0] - 1 or j == 0 or j == img.shape[1] - 1:
                img_border[i][j] = 0  # ��������� ������� � �������� 0
            # ����������� �������� �� ���� � ����������� �� �������� ���� ���������
            else:
                x_shift = 0
                y_shift = 0
                # �������� �� ��� �������
                if angle == 0 or angle == 4:
                    x_shift = 0
                elif angle > 0 and angle < 4:
                    x_shift = 1
                else:
                    x_shift = -1
                # �������� �� ��� �������
                if angle == 2 or angle == 6:
                    y_shift = 0
                elif angle > 2 and angle < 6:
                    y_shift = -1
                else:
                    y_shift = 1
                # �������� �������� �� ������� ������������ �������� ���������
                is_max = gradient >= matr_gradient[i + y_shift][j + x_shift] and gradient >= matr_gradient[i - y_shift][ j - x_shift]
                img_border[i][j] = 255 if is_max else 0
    cv2.imshow('img_border ' + str(i), img_border)

    lower_bound = max_gradient / bound_path
    upper_bound = max_gradient - max_gradient / bound_path
    double_filtration = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            gradient = matr_gradient[i][j]
            # �������� ��������� �� ������� �� ������� �����������
            if img_border[i][j] == 255:
                # �������� ��������� � ���������
                if gradient >= lower_bound and gradient <= upper_bound:
                    flag = False
                    # �������� ������� � ������������ ������ ��������� ����� �������
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            if flag:
                                break
                            # ����� �������
                            if img_border[i + k][j + l] == 255 and matr_gradient[i + k][j + l] >= lower_bound:
                                flag = True
                                break
                    if flag:
                        double_filtration[i][j] = 255
                # ���� �������� ��������� ���� - ������� �������, �� ������� ����� �������
                elif gradient > upper_bound:
                    double_filtration[i][j] = 255
    cv2.imshow('Double_filtration ' + str(i), double_filtration)

    cv2.waitKey(0)



main('curry.jpg', 3, 3, 5)
#main('curry.jpg', 6, 5, 10)
#main('curry.jpg', 100, 9, 15)