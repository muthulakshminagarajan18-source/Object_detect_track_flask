from flask import Flask, render_template, Response, jsonify
from ultralytics import YOLO
import cv2

app = Flask(__name__)

# Load YOLOv8n model (downloads automatically if not present)
model = YOLO("yolov8n.pt")

# Global variables for tracking
previous_objects = set()

# Video capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Could not open webcam")

def gen_frames():
    global previous_objects
    while True:
        success, frame = cap.read()
        if not success:
            break

        # Run YOLO detection
        results = model(frame)
        annotated_frame = results[0].plot().copy()

        # Extract object labels
        current_objects = [results[0].names[int(cls)] for cls in results[0].boxes.cls]

        # Detect new objects
        previous_objects = set(current_objects)

        # Encode frame as JPEG
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_objects')
def get_objects():
    # Return current object counts
    counts = {}
    for obj in previous_objects:
        counts[obj] = counts.get(obj, 0) + 1
    return jsonify(counts)

if __name__ == '__main__':
    app.run(debug=True)
