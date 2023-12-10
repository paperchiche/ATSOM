# -*- coding: cp1251 -*-
import tensorflow as tf
from keras.models import load_model
from keras.datasets import mnist
from keras.utils import to_categorical
import time

# �������� ������ ������������� ����� �����������
model = load_model("./models/multilayer_perceptron.keras")

# ����� ������ ������� ������
start_time = time.time()

# ������� ���������� ��� ���������
epochs_list = [1, 2, 3]  # �����
learning_rates = [0.001, 0.01, 0.1]  # �������� ��������
num_layers_list = [1, 2, 3]  # ����
accuracies = [] # ��������

# �������� ������ MNIST (������ ������ - ������������� ����������� � �����, � ������ - �������� ����������� � �����)
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# �������������� ����������� � ���������� ������� � ������������
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255
#�������������� ����������� � ���������� �������
train_images_flat = train_images.reshape((60000, 784))
test_images_flat = test_images.reshape((10000, 784))

# � ���� ������ MNIST ���������� 10 ������� ���� �� 0 �� 9
num_classes = 10
# �������������� ����� � ��������� ��� ������� ���� ������
train_labels = to_categorical(train_labels, num_classes)
test_labels = to_categorical(test_labels, num_classes)

# ������� ��������� �������� ����, ��������� �������� � ���������� �����
for epochs in epochs_list:
    for lr in learning_rates:
        for num_layers in num_layers_list:
            # �������� ������ � ������������ ����������� �����
            layered_model = tf.keras.Sequential()
            for _ in range(num_layers):
                layered_model.add(tf.keras.layers.Dense(128, activation='relu'))
            layered_model.add(tf.keras.layers.Dense(10, activation='softmax'))

            # ���������� ������
            layered_model.compile(optimizer=tf.keras.optimizers.RMSprop(learning_rate=lr),
                                  loss='categorical_crossentropy',
                                  metrics=['accuracy'])

            # �������� ������
            layered_model.fit(train_images_flat, train_labels, epochs=epochs, batch_size=128, verbose=0)

            # ������ ������ �� �������� ������
            test_loss, test_accuracy = layered_model.evaluate(test_images_flat, test_labels, verbose=0)

            # ���������� ���������� � ������ accuracies
            accuracies.append((epochs, lr, num_layers, test_accuracy))

    print('=================================================================================================================')

    # ����� �����������
    for epochs, lr, num_layers, accuracy in accuracies:
        print(f'�����: {epochs}, �������� ��������: {lr}, ���������� �����: {num_layers}, �������� �� �����: {accuracy}')


# ������� ������������ �������
end_time = time.time()
print('����������� �����:', end_time - start_time)
print('=================================================================================================================')