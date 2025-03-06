import cv2
import numpy as np
face_cap = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
if face_cap.empty():
    print("Error: Haarcascade file not found.")
    exit()
video_cap = cv2.VideoCapture(0)
if not video_cap.isOpened():
    print("Error: Could not open webcam.")
    exit()
prev_x, prev_y, prev_w, prev_h = None, None, None, None
alpha = 0.6  
while True:
    ret, video_data = video_cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    video_data = cv2.flip(video_data, 1)
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(col, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        if prev_x is not None:
            x = int(alpha * prev_x + (1 - alpha) * x)
            y = int(alpha * prev_y + (1 - alpha) * y)
            w = int(alpha * prev_w + (1 - alpha) * w)
            h = int(alpha * prev_h + (1 - alpha) * h)
        prev_x, prev_y, prev_w, prev_h = x, y, w, h
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (255, 255, 255), 2)
    cv2.imshow("video_live", video_data)
    if cv2.waitKey(10) == ord("a"):
        break
video_cap.release()
cv2.destroyAllWindows()
