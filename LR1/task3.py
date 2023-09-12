# Задание 3. Отобразить видео в окне. Рассмотреть методы класса
# VideoCapture и попробовать отображать видео в разных форматах, в частности
# размеры и цветовая гамма.

import cv2

cap = cv2.VideoCapture(r'C:\Users\20art\Videos\Captures\video1.mp4')
# если указать 0, то будет вебка
# cap = cv2.VideoCapture(0)

# cv2.CAP_PROP_BRIGHTNESS - яркость (0-1)
# cv2.CAP_PROP_CONTRAST - контраст (0-1)
# cv2.CAP_PROP_SATURATION - насыщенность (0-1)
# cv2.CAP_PROP_HUE - оттенок (0-1)

cap.set(cv2.CAP_PROP_BRIGHTNESS, 0.5)
cap.set(cv2.CAP_PROP_CONTRAST, 0.8)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)

while True:
    # Захват кадра из видеопотока.
    ret, frame = cap.read()

    if not ret:
        print("Конец видео")
        break

    # Отображение кадра на экране.
    resize = cv2.resize(frame, (640, 360))  # изменение расширения
    cv2.normalize(frame, frame, 0, 277, cv2.NORM_MINMAX)
    cv2.imshow("Video", resize)

    # Выход на q.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Освобождение памяти
cap.release()
cv2.destroyAllWindows()