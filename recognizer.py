"""
recognizer.py - Face recognition + attendance marking
Fixes applied:
  - Removed unused firebase import
  - Fixed 'y10' bug -> 'y-10'
  - Added student name mapping dict (edit this to match your students)
"""
import cv2
import numpy as np
import xlwrite
import time

# ── CONFIG ──────────────────────────────────────────────────────────────────
# Map numeric IDs (assigned during dataset capture) to student names
STUDENT_NAMES = {
    1: "Y Deepthanshu",
    2: "D Sushma",
    3: "V Lakshmi Prasanna",
    4: "C Preethi",
    5: "k Punarvika",
    6: "Rithvika"
    # Add more as needed: ID: "Name"
}

CONFIDENCE_THRESHOLD = 50   # Lower = stricter match
SESSION_DURATION     = 30   # Seconds to run recognition
# ────────────────────────────────────────────────────────────────────────────

face_cas   = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap        = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

font       = cv2.FONT_HERSHEY_SIMPLEX
start      = time.time()
marked     = {}   # Tracks who has already been marked present

print("Starting recognition. Press 'q' to quit.")

while True:
    ret, img = cap.read()
    if not ret:
        print("Camera not accessible.")
        break

    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cas.detectMultiScale(gray, 1.3, 7)

    for (x, y, w, h) in faces:
        roi_gray    = gray[y:y + h, x:x + w]
        student_id, conf = recognizer.predict(roi_gray)

        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        if conf < CONFIDENCE_THRESHOLD:
            name = STUDENT_NAMES.get(student_id, f"ID_{student_id}")

            # Mark attendance only once per session
            if str(student_id) not in marked:
                xlwrite.output('attendance', 'class1', student_id, name, 'yes')
                marked[str(student_id)] = name

            label = f"{name}  ({round(conf, 1)})"
        else:
            label = "Unknown"

        cv2.putText(img, label, (x, y - 10), font, 0.6, (120, 255, 120), 2)

    cv2.imshow('Face Recognition Attendance', img)

    # Stop after SESSION_DURATION seconds or 'q' key
    if time.time() > start + SESSION_DURATION:
        print("Session complete.")
        break
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(f"Attendance marked for: {list(marked.values())}")
