import cv2
from ultralytics import YOLO
from matplotlib import pyplot as plt
import keyboard 
import numpy as np

import chatgptimage

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")
# Initialize the webcam
cap = cv2.VideoCapture(0)

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the image from BGR (OpenCV format) to RGB
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Inference
        results = model(img_rgb)
        names = results[0].names

        # Results
        boxes = np.array(results[0].boxes.xyxy.cpu())
        conf = np.array(results[0].boxes.conf.cpu())
        label = np.array([names[int(val)] for val in results[0].boxes.cls.cpu()])

        # Draw bounding boxes and labels on the image
        for label, cord in zip(label, boxes):
            x1, y1, x2, y2 = cord
            start_point = (int(x1), int(y1))
            end_point = (int(x2), int(y2))
            color = (0, 255, 0)
            thickness = 2
            frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
            cv2.putText(
                frame,
                f"{label}",
                (int(x1), int(y1 - 10)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                color,
                2,
            )

        # Display the resulting frame
        cv2.imshow("YOLOv8 Webcam", frame)

        # Break the loop with the 'q' key
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        if keyboard.is_pressed('s'):
            cv2.imwrite("image.jpg", frame)
            chatgptimage.understand_image("image.jpg")
            break

finally:
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
