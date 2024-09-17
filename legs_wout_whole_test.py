from ultralytics import YOLO
model= YOLO('C:/Users/dell/Downloads/Nike/legs_wout_whole/legs_wout_whole.pt')
results=model(source=0,show=True,conf=0.6,save=True)
#'C:/Users/dell/Downloads/Nike/Predict_Numbers/chair/table legs/chair/chair_3c0.jpeg'