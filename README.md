
# 🛋️ Furniture Leg Detection Project 

## 🚀 Overview

Welcome to the **Furniture Leg Detection Project**! This project leverages advanced **object detection** to identify and track furniture legs in images and videos. Whether you're looking to automate **inventory management**, enhance **quality control**, or implement **augmented reality** applications, this system provides robust solutions! 💡

### 🔑 Key Features
- 📦 **Custom Dataset**: Annotated with **Roboflow** for high accuracy.
- 🔍 **YOLOv8 & YOLOv9**: Leveraging the power of state-of-the-art object detection frameworks for precise performance.
- 🎥 **Real-Time Detection**: Supports both **image** and **video** input, perfect for live applications.
- 🎯 **Confidence Threshold Adjustment**: Fine-tune detection results for optimal accuracy.
- 💾 **Auto-Save Results**: Detected items are automatically saved for further analysis.

---

## ⚙️ Technologies Used

- **Python**: The programming language that powers the project. 🐍
- **YOLOv8 & YOLOv9**: Cutting-edge object detection frameworks for accuracy and speed. ⚡
- **OpenCV**: Real-time image processing library for video capture and manipulation. 📸
- **Roboflow**: Tool for dataset annotation and preprocessing, enhancing model quality. 📝

---

## 🛠️ How It Works

1. **Dataset Preparation**: Annotate the dataset of furniture legs using **Roboflow** and export it for training. 🖼️
2. **Model Training**: Train the **YOLO** model with the annotated data, teaching it to detect patterns of furniture legs. 💡
3. **Detection**: Use the trained model to detect furniture legs in images and videos, displaying bounding boxes and tracking objects in real time. 🎯

---

## 💻 Code Example

Here’s a quick look at how the detection works in action:

```python
from ultralytics import YOLO

# Load the pre-trained model
model = YOLO('C:/Users/dell/Downloads/Nike/legs_wout_whole/legs_wout_whole.pt')

# Perform detection on live video (e.g., webcam feed)
results = model(source=0, show=True, conf=0.6, save=True)
```

---

## 🏃‍♂️ How to Run

1. **Install Dependencies**:
   Install the required libraries via pip:
   ```bash
   pip install ultralytics opencv-python
   ```
2. **Download the Model**:
   - Get the trained model [here](https://drive.google.com/file/d/1X4YulpSKUdRvk0FL24E-lGNJq1mTnhwF/view?usp=sharing).
   - Save the `.pt` file to a known directory. 🗂️

3. **Run the Script**:
   - Update the script with the correct path to your downloaded model.
   - Execute the script with:
     ```bash
     python detect_furniture_legs.py
     ```

4. **Results**:
   - The model will display **live detections** on your video feed! 📹
   - Detected frames will be saved to the output directory. 📂

---

## 🌍 Example Use Case

**Input**: An image or video of a room filled with furniture. 🛏️🪑

**Output**:  
- Bounding boxes around the detected furniture legs.  
- Saved results with annotated images or videos. 📸

---

## ⚠️ Notes

- Ensure that your **input source** (camera or video file) is properly configured. 🎥
- Adjust the **confidence threshold** (`conf` parameter) for fine-tuning detection. 🎯

---

## 🚀 Future Improvements

- Expand the model to detect **other furniture components** (e.g., tables, chairs). 🪑
- Integrate with **IoT devices** for **automated inventory tracking**. 🏠
- Develop a **user-friendly interface** for non-technical users to easily interact with the model. 💻
