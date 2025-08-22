# src/face_detection.py
import cv2
from pathlib import Path
import argparse

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL = Path(BASE_DIR, "models", "haarcascade_frontalface_default.xml")

cascade_path = Path(__file__).parent.parent / "models" / "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(str(cascade_path))
print("Cascade loaded:", not face_cascade.empty())

def detect_in_image(img_path, out_path=None):
    face_cascade = cv2.CascadeClassifier(str(cascade_path))
    img = cv2.imread(str(img_path))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40,40))
    
    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # ✅ Add these lines here to preview the image
    cv2.imshow("Annotated Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Save the annotated image if output path is provided
    if out_path:
        cv2.imwrite(str(out_path), img)


def webcam_detect():
    face_cascade = cv2.CascadeClassifier(str(MODEL))
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open webcam")
        return
    print("Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(40,40))
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("Webcam Face Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", help="path to image file")
    parser.add_argument("--out", help="path to save annotated image")
    parser.add_argument("--webcam", action="store_true", help="use webcam")
    args = parser.parse_args()

    if args.webcam:
        webcam_detect()
    elif args.image:
        detect_in_image(args.image, args.out)
    else:
        print("Use --image <path> or --webcam")
