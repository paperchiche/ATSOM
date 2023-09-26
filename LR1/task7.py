# Задание 7 (самостоятельно) Отобразить информацию с вебкамеры, записать видео в файл, продемонстрировать видео.

import cv2
cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print("Ошибка при открытии вебкамеры")
    exit()


output_file = "task_7.avi"  # Имя выходного файла
frame_width = int(cap.get(3))  # Ширина кадра
frame_height = int(cap.get(4))  # Высота кадра
fps = 30.0  # Количество кадров в секунду


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

while True:

    ret, frame = cap.read()

    if not ret:
        print("Ошибка при захвате кадра.")
        break

    cv2.imshow("Webcam Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()