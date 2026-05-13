"""
training_dataset.py - Train the LBPH face recognizer on captured dataset
Reads images from dataset/, trains the model, saves to trainer/trainer.yml
"""
import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector   = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def getImagesAndLabels(path):
    image_paths  = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
    face_samples = []
    ids          = []

    for image_path in image_paths:
        filename = os.path.split(image_path)[-1]

        # Skip files that don't match User.ID.count.jpg format
        parts = filename.split(".")
        if len(parts) < 3 or not parts[1].isdigit():
            print(f"Skipping invalid file: {filename}")
            continue

        pil_img  = Image.open(image_path).convert('L')
        img_np   = np.array(pil_img, 'uint8')
        face_id  = int(parts[1])
        faces    = detector.detectMultiScale(img_np)

        for (x, y, w, h) in faces:
            face_samples.append(img_np[y:y+h, x:x+w])
            ids.append(face_id)

    return face_samples, ids


print("Training... please wait.")
faces, ids = getImagesAndLabels('dataset')

if len(faces) == 0:
    print("No faces found in dataset/. Run 'Create Dataset' first.")
else:
    os.makedirs("trainer", exist_ok=True)
    recognizer.train(faces, np.array(ids))
    recognizer.write('trainer/trainer.yml')
    print(f"Training complete! {len(faces)} face samples trained.")
