import cv2

output_file = "output_video.avi"  # Имя выходного файла
frame_width = 1280  # Ширина кадра
frame_height = 720  # Высота кадра
fps = 30.0  # Количество кадров в секунду

cap = cv2.VideoCapture(r'C:\GitHub\ATSOM\LR1\video01.mp4')

if not cap.isOpened():
    print("Ошибка при открытии вебкамеры.")
    exit()

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # кодек (XVID для AVI)
out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()

    if not ret:
        print("Ошибка при захвате кадра.")
        break

    # Запись кадра в выходное видео
    out.write(frame)

    # зеркало
    cv2.imshow("Video", frame)

    # выход
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# выход
cap.release()
out.release()
cv2.destroyAllWindows()