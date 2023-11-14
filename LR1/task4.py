# -*- coding: cp1251 -*-
import cv2

# Параметры для входного видео
input_file = r"C:\GitHub\ATSOM\LR1\video01.mp4"

# Параметры для выходного видео
output_file = "output_video.avi"
frame_width = 1280  # Ширина кадра
frame_height = 720  # Высота кадра
fps = 30  # Количество кадров в секунду

# Открываем входное видео
cap = cv2.VideoCapture(input_file)

# Проверяем, успешно ли открыто видео
if not cap.isOpened():
    print("Ошибка при открытии видео.")
    exit()

# Получаем размеры кадра из входного видео
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Определяем кодек и создаем объект VideoWriter для записи выходного видео
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

# Читаем кадры из входного видео и записываем их в выходное видео
while True:
    ret, frame = cap.read()

    # Проверяем, успешно ли считан кадр
    if not ret:
        print("Ошибка при захвате кадра.")
        break

    # Записываем кадр в выходное видео
    out.write(frame)

    # Отображаем кадр
    cv2.imshow("Video", frame)

    # Выход по нажатию клавиши 'q' с задержкой 25 миллисекунд
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
cap.release()
out.release()
cv2.destroyAllWindows()
