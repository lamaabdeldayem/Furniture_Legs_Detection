# README: Furniture Leg Detection Project

## Overview
This project is designed to detect furniture legs in images and videos using a custom-trained object detection model. The model identifies and tracks furniture legs in various scenarios, enabling applications such as inventory management, quality control, and augmented reality.

### Key Features
- Utilizes a custom dataset annotated with Roboflow for high accuracy.
- Leverages advanced object detection models (YOLOv8, YOLOv9) for robust performance.
- Supports both image and real-time video input.
- Includes confidence threshold adjustment for fine-tuning detection.
- Automatically saves detection results.

## Technologies Used
- **Python**: Programming language for implementation.
- **YOLOv8 & YOLOv9**: State-of-the-art object detection frameworks.
- **OpenCV**: Real-time image processing library.
- **Roboflow**: Dataset annotation and preprocessing tool.

## How It Works
1. **Dataset Preparation**: The dataset of furniture legs is annotated using Roboflow and exported for model training.
2. **Model Training**: A YOLO model is trained using the annotated dataset to learn the patterns of furniture legs.
3. **Detection**: The trained model detects furniture legs in images and videos, outputs results with bounding boxes, and tracks objects in real time.

## Code Example
Below is a snippet of the main detection logic:

```python
from ultralytics import YOLO

# Load the pre-trained model
model = YOLO('C:/Users/dell/Downloads/Nike/legs_wout_whole/legs_wout_whole.pt')

# Perform detection on live video (e.g., webcam feed)
results = model(source=0, show=True, conf=0.6, save=True)
```

## How to Run
1. **Install Dependencies**:
   Install required libraries using pip:
   ```bash
   pip install ultralytics opencv-python
   ```
2. **Download the Model**:
   - Access the trained model from the following link: [Download Model](https://drive.google.com/file/d/1X4YulpSKUdRvk0FL24E-lGNJq1mTnhwF/view?usp=sharing).
   - Save the `.pt` file to a known directory.

3. **Run the Script**:
   - Update the model path in the script to point to your downloaded `.pt` file.
   - Execute the script:
     ```bash
     python detect_furniture_legs.py
     ```

4. **Results**:
   - The model displays live detections on the video feed.
   - Detected frames are saved to the output directory.

## Example Use Case
**Input**:
An image or video of a room containing furniture.

**Output**:
- Bounding boxes around detected furniture legs.
- Saved results with annotated images or video.

## Notes
- Ensure the input source (camera or video file) is correctly configured.
- The model’s confidence threshold can be adjusted (`conf` parameter) for better precision or recall.

## Future Improvements
- Enhance the model to detect other furniture components.
- Integrate with IoT devices for automated inventory tracking.
- Develop a user-friendly interface for non-technical users.

