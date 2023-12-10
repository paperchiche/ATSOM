# -*- coding: cp1251 -*-
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import time

start_time = time.time()

# �������� ������ MNIST (������ ������ - ������������� ����������� � �����, � ������ - �������� ����������� � �����)
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# ������������ ������
train_images = train_images / 255.0
test_images = test_images / 255.0

# ��������� ����� �������� �� ��������� � �������������, �������� ����������� ������
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

# �������� ������ ���������� ��������� ����
model = models.Sequential()
# ���������� ������� ����
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
# ���������� ���� ������� - �.�. ���������� ����������� ������������ ���������, ����������� ���������� ���������� � ���������� � ����, �������������, �������������� ������������.
model.add(layers.MaxPooling2D((2, 2)))
# ���������� ������� ����
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
# ���������� �������� ����
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# ���������� ���� �������������� - �.�. �������������� ����������� ������ � ���������� ������, ��� ��������� ���������� ������ � ������������ ����
model.add(layers.Flatten())
# ���������� ��������� ����
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10))

# ��������� �������� �������� ������
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# # ���������� TensorBoard � ������
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="C:\GitHub\ATSOM")

# �������� ������ �� ������������� ������
history = model.fit(train_images, train_labels,
                    epochs=5,
                    validation_data=(test_images, test_labels),
                    callbacks=[tensorboard_callback])

print('==============================================================')
# ������ ������ � �������� ������
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('������ �� �������� ������:', test_loss)
print('�������� ������ �� �������� ������:', test_acc)

# ������� �������� ���������� ������ �� �������� ����
accuracy = test_acc
percent_correct = accuracy * 100
print('������� ���������� ������:', percent_correct)

# ������� ������������ �������
end_time = time.time()
print('����������� �����:', end_time - start_time)
print('==============================================================')