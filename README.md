# Face Detection Project 👤📷

## Overview

This project implements **real-time face detection** using **OpenCV** in Python.
It supports both **Haarcascade Classifier** and **OpenCV DNN-based face detection**, allowing detection from:

* Single images
* Multiple images
* Webcam stream

The project is designed to be **industry-ready**, with a clean folder structure, CLI support, and easy extension to advanced models.

---

## Tech Stack

* Python 3.x
* OpenCV (cv2)
* NumPy
* Matplotlib (optional, for visualization)

Optional for future enhancements:

* OpenCV DNN / MTCNN
* Flask / Streamlit for web deployment

---

## Features

* Real-time **face detection** from webcam
* Detect faces in single or multiple images
* Saves annotated images in `results/`
* Modular and extendable codebase for adding **emotion recognition** or **face recognition**
* Clean **GitHub-ready structure** with `requirements.txt` and `.gitignore`

---

## Project Structure

```text
Face-Detection-Project/
├── data/                 # sample images/videos
├── models/               # Haarcascade XML or DNN weights
├── src/                  # source code
│   └── face_detection_dnn.py
├── notebooks/            # optional Jupyter experiments
├── results/              # annotated output images/videos
├── README.md             # project documentation
├── requirements.txt      # dependencies
└── .gitignore
```

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/Face-Detection-Project.git
cd Face-Detection-Project
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Download models** (if not included)

* Haarcascade XML is already included in `models/`.
* For DNN, download manually or using script:

```text
deploy.prototxt
res10_300x300_ssd_iter_140000.caffemodel
```

---

## Usage

### Run on a single image

```bash
python src/face_detection_dnn.py --image data/sample.jpg --out results/annotated.jpg
```

### Run on multiple images

```bash
python src/face_detection_dnn.py --images data/img1.jpg data/img2.jpg --out results/
```

### Run on webcam

```bash
python src/face_detection_dnn.py --webcam
```

* Press **'q'** to quit the webcam stream

---

## Screenshots / Demo

![Webcam Detection](results/demo_webcam.png)
*Webcam detection in real-time*

![Image Detection](results/annotated.jpg)

*Face detection on a sample image*

---

## Future Enhancements

* **Emotion Recognition** using OpenCV / Deep Learning
* **Face Recognition** with Dlib / FaceNet
* **Web App Deployment** with Flask / Streamlit
* **Cloud Deployment** (Heroku / AWS / Streamlit Cloud)
* **Batch image processing** and logging statistics

---

## License

MIT License © 2025 Muskan Singh

---

## CV / Portfolio Description Example

**Face Detection System (Python, OpenCV, DNN):**
Built a real-time face detection project capable of detecting faces in images and webcam feed. Designed industry-level project structure with modular code, README documentation, and GitHub-ready folder structure. Extended for future enhancements like emotion recognition and cloud deployment.




