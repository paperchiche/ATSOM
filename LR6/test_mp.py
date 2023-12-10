# -*- coding: cp1251 -*-
from keras.models import load_model
import cv2
import numpy as np

# �������� ������ ������������� ����� �����������
model = load_model("./models/multilayer_perceptron.keras")

# �������� ������������ ����������� � �������� ������
image_path = "input_picture/2.jpg"
img_cv = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# ��������� ������� ����������� �� 28x28 (���������� ������� MNIST �����������)
img_cv = cv2.resize(img_cv, (28, 28))
# ������ ������� ����������� (������ ���� (28, 28))
print('������ ������������ �����������:',img_cv.shape)
# ������������ �����������
image = img_cv / 255.0
# ������� ����������� � ���������� ������
image = image.reshape(1, 784)

# ��������� ������������ ������ ��� �����������
predictions = model.predict(image)
# ����� ������������� ������������ ��� ������� ������ ����
print(predictions)
# ��������� ������� ������ � ���������� ������������
predicted_class = np.argmax(predictions)

# ����� �������������� ������(�����)
print(f"������������� �����: {predicted_class}")