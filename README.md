# Real-Time Object Detection with YOLOv8

A simple Python project that detects multiple objects using **YOLOv8 (Ultralytics)** and **OpenCV**. It works with a laptop webcam, a phone camera, images, and videos. Each detected object gets a colored bounding box with its name and confidence score shown below it.

## Features

- Live detection from the **laptop webcam**
- Live detection from a **phone camera** over Wi-Fi
- Detection on **images** and **videos**
- Detects **multiple objects at once** (80 COCO classes: person, car, bottle, laptop, etc.)
- Colored box per class, with the **label displayed below the box**
- Runs at up to **30 FPS** in live mode (depends on your hardware)

## Demo

<!-- Add your screenshots or GIFs here, for example: -->
<!-- ![Demo](screenshots/demo.png) -->

## Requirements

- Python 3.8 or higher
- A webcam (optional) and a phone with an IP camera app (optional)

## Installation

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
pip install ultralytics opencv-python
```

The YOLOv8 model (`yolov8n.pt`) is downloaded automatically the first time you run the script.

## Usage

```bash
python detect_simple.py 0                  # laptop webcam
python detect_simple.py 192.168.1.5:8080   # phone camera
python detect_simple.py photo.jpg          # image
python detect_simple.py video.mp4          # video
```

Press **q** to close the window. Detected images are saved as `result.jpg`.

### Using your phone as a camera

1. Install an IP camera app such as **IP Webcam** (Android) or **Iriun / DroidCam** (Android and iOS).
2. Connect your phone and laptop to the **same Wi-Fi network**.
3. Start the server in the app and note the address it shows (for example `192.168.1.5:8080`).
4. Run `python detect_simple.py 192.168.1.5:8080`.

## How It Works

1. A frame is read from the camera, image, or video file using OpenCV.
2. The frame is passed to the YOLOv8 model, which returns the bounding boxes, class names, and confidence scores.
3. Each detection is drawn as a colored rectangle with its label below it.
4. The annotated frame is displayed, and the loop is limited to about 30 FPS.

## Tech Stack

- [Python](https://www.python.org/)
- [Ultralytics YOLOv8](https://docs.ultralytics.com/)
- [OpenCV](https://opencv.org/)

## Tips

- For better accuracy, change `yolov8n.pt` to `yolov8s.pt` or `yolov8m.pt` in the script (slower but more accurate).
- If the FPS is low on a CPU-only laptop, use a smaller model or a lower-resolution camera.
- Use a GPU (CUDA) for the smoothest real-time performance.

## Future Improvements

- Object counting and tracking
- Training on a custom dataset
- Saving annotated videos from live streams
- Alerts for specific objects

## Author

**Devaki**
GitHub: [@devakisan_hub](https://github.com/devakisan-hub)
