import sys
import time
import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # downloads automatically the first time

# Source: 0 = laptop cam | 192.168.1.5:8080 = phone cam | photo.jpg | video.mp4
src = sys.argv[1] if len(sys.argv) > 1 else "0"
if src.isdigit():
    src = int(src)
elif src.replace(".", "").replace(":", "").isdigit():  # phone IP address
    src = f"http://{src}/video"


def detect(frame):
    """Draw a colored box around each object with its name below the box."""
    h = frame.shape[0]
    for b in model(frame, conf=0.4, verbose=False)[0].boxes:
        x1, y1, x2, y2 = map(int, b.xyxy[0])
        c = int(b.cls[0])
        color = ((c * 47) % 200 + 55, (c * 91) % 200 + 55, (c * 133) % 200 + 55)
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        label = f"{model.names[c]} {float(b.conf[0]):.0%}"
        cv2.putText(frame, label, (x1, min(y2 + 22, h - 6)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
    return frame


if isinstance(src, str) and src.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".webp")):
    img = detect(cv2.imread(src))              # picture
    cv2.imwrite("result.jpg", img)
    cv2.imshow("YOLOv8", img)
    cv2.waitKey(0)
else:
    cap = cv2.VideoCapture(src)                # webcam / phone / video file
    cap.set(cv2.CAP_PROP_FPS, 30)
    while True:
        start = time.time()
        ok, frame = cap.read()
        if not ok:
            break
        frame = detect(frame)
        cv2.imshow("YOLOv8 (press q to quit)", frame)
        delay = max(1, int((1 / 30 - (time.time() - start)) * 1000))  # hold ~30 FPS
        if cv2.waitKey(delay) & 0xFF == ord("q"):
            break
    cap.release()

cv2.destroyAllWindows()
