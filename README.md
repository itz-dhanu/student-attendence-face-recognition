# 🎓 Student Attendance System Using Face Recognition

> A real-time automated attendance system using OpenCV and LBPH face recognition algorithm built with Python.

---

## 👥 Team Members

| Roll No | Name |
|---------|------|
| 227Y1A6141 | Y Dhanusree |
| 227Y1A6142 | Yadadhala Kavitha |
| 227Y1A6143 | Chakali Harish Kumar |
| 227Y1A6144 | Ediga Ravi |
| 227Y1A6145 | Uppaluri Siva Sankar Reddy |
| 227Y1A6146 | Vallem Venkata Pavan |

**Guide:** Ms. M. Nazhiya M.Tech, Assistant Professor  
**Institution:** AI Global Institute of Engineering & Technology  
**Department:** Artificial Intelligence and Machine Learning Engineering  
**Year:** 2022–2026

---

## 📌 Abstract

This project implements an automated student attendance system using face detection and recognition. The system uses OpenCV's LBPH (Local Binary Pattern Histogram) algorithm to detect and recognize student faces in real time via webcam and automatically marks their attendance in an Excel sheet — replacing the traditional manual attendance process.

---

## ⚙️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python 3.10 | Core programming language |
| OpenCV (opencv-contrib-python) | Face detection & recognition |
| LBPH Algorithm | Face recognition model |
| Haar Cascade Classifier | Face detection |
| Tkinter | GUI interface |
| xlwt / xlrd | Excel attendance sheet generation |
| Pillow | Image processing |
| NumPy | Numerical operations |

---

## 📁 Project Structure

```
attendance_project/
│
├── frontpage.py          ← Main GUI (run this to start)
├── dataset_capture.py    ← Captures face images per student
├── training_dataset.py   ← Trains LBPH model on captured images
├── recognizer.py         ← Live face recognition + attendance marking
├── xlwrite.py            ← Excel attendance writer module
├── requirements.txt      ← All dependencies
│
├── dataset/              ← Stores captured face images
├── trainer/              ← Stores trained model (trainer.yml)
└── firebase/
    └── attendance_files/ ← Stores daily Excel attendance sheets
```

---

## 🚀 How to Run

### Step 1 — Install Python
Download Python 3.8–3.10 from https://www.python.org/downloads/
> ✅ Check **"Add Python to PATH"** during installation

### Step 2 — Clone the Repository
```bash
git clone https://github.com/yourusername/attendance-system.git
cd attendance-system
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```
> ⚠️ Use `opencv-contrib-python` NOT `opencv-python` — required for the face recognizer module

### Step 4 — Add Student Names
Open `recognizer.py` and update:
```python
STUDENT_NAMES = {
    1: "Y Dhanusree",
    2: "Yadadhala Kavitha",
    3: "Chakali Harish Kumar",
    4: "Ediga Ravi",
    5: "Uppaluri Siva Sankar Reddy",
}
```

### Step 5 — Run the System
```bash
python frontpage.py
```

---

## 🖥️ System Flow

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   1. Create Dataset                                 │
│      └── Webcam captures 30 face photos/student     │
│                                                     │
│   2. Train Dataset                                  │
│      └── LBPH model learns from captured photos     │
│                                                     │
│   3. Recognize + Attendance                         │
│      └── Webcam detects face → matches with model   │
│      └── Name displayed → marked Present in Excel   │
│                                                     │
│   4. Attendance Sheet                               │
│      └── Opens daily Excel attendance file          │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 📊 Results

- ✅ Real-time face detection using Haar Cascade Classifier
- ✅ Face recognition using LBPH algorithm
- ✅ Automated Excel attendance sheet generation
- ✅ Each student marked only once per session
- ✅ Simple and user-friendly GUI

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| `No module named 'cv2.face'` | Run `pip install opencv-contrib-python` |
| `xlrd` version error | Run `pip install xlrd==1.2.0` |
| Camera not opening | Change `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` |
| Recognition shows Unknown | Retrain with clearer, well-lit photos |
| Low training samples | Ensure face is clearly visible during capture |

---

## 🔮 Future Enhancements

- Anti-spoofing using eye blink detection
- Monthly attendance report generation
- Email alerts for low attendance students
- Web dashboard for attendance analytics
- Multi-camera support for large classrooms

---

## 📚 References

1. P. Viola and M. Jones, "Rapid Object Detection using a Boosted Cascade of Simple Features," 2001
2. Ahonen et al., "Face Recognition with Local Binary Patterns," ECCV 2004
3. OpenCV Documentation — https://docs.opencv.org

---

## 📄 License

This project is developed for academic purposes at AI Global Institute of Engineering & Technology, Markapur.
