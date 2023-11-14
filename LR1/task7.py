# Задание 7 (самостоятельно) Отобразить информацию с вебкамеры, записать видео в файл, продемонстрировать видео.
import cv2

cap = cv2.VideoCapture(0)

# Параметры для записи видео
output_file = "task_7.avi"
frame_width = int(cap.get(3))  # Ширина кадра
frame_height = int(cap.get(4))  # Высота кадра
fps = 30  # Количество кадров в секунду

# Определяем кодек и создаем объект VideoWriter для записи выходного видео
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

while True:
    # Читаем кадр с вебкамеры
    ret, frame = cap.read()

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
