# -*- coding: cp1251 -*-
import numpy as np
from scipy.ndimage import gaussian_filter

# ������� ��� �������� � ������ ������� �������
def create_and_print_gaussian_kernel(size, sigma):
    kernel = gaussian_filter(np.zeros((size, size), dtype=np.float32), sigma)
    print(f"Gaussian Kernel (Size: {size}, Sigma: {sigma}):")
    print(kernel)
    print()

# ������ ������� � ����� ��� ������ �������
sizes = [3, 5, 7]
sigmas = [1.0, 1.5, 2.0]

# ������� � ������� ������� �������
for size in sizes:
    for sigma in sigmas:
        create_and_print_gaussian_kernel(size, sigma)