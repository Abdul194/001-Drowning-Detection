import cv2
import time
import os

i = 0
v = 0
for file in os.listdir("./Drowning Video"):
    if file.endswith(".mp4"):
        path = os.path.join("Drowning Video", file)
        print(path)

        cap = cv2.VideoCapture(path)

        frame_rate = 1
        prev = 0

        while cap.isOpened():
            time_elapsed = time.time() - prev
            ret, frame = cap.read()
            if not ret:
                break

            if time_elapsed > 1. / frame_rate:
                # print(time_elapsed)
                prev = time.time()
                cv2.imwrite('./abcd/frame' + str(v) + '-' + str(i) + '.jpg', frame)
                i += 1
        v += 1
        cap.release()
        cv2.destroyAllWindows()


