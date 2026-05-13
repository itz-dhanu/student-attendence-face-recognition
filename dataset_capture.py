"""
dataset_capture.py - Capture face images for training
Captures 30 grayscale face images per student and saves to dataset/
"""
import cv2
import os

def assure_path_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

face_id = input("Enter your numeric ID (e.g. 1 for Student 1): ").strip()

vid_cam = cv2.VideoCapture(0)
vid_cam.set(3, 640)
vid_cam.set(4, 480)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

count = 0
assure_path_exists("dataset/")

print("Look at the camera. Capturing 30 images... Press 'q' to cancel.")

while True:
    _, image_frame = vid_cam.read()
    gray  = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1
        cv2.imwrite(f"dataset/User.{face_id}.{count}.jpg", gray[y:y+h, x:x+w])

    cv2.putText(image_frame, f"Samples: {count}/30", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.imshow('Capturing Dataset - Press Q to quit', image_frame)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    elif count >= 30:
        print("Successfully captured 30 samples!")
        break

vid_cam.release()
cv2.destroyAllWindows()
