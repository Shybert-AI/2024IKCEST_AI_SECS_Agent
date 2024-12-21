# #https://blog.csdn.net/qq_42452134/article/details/135241059
import cv2
from ultralytics import YOLO
import os
import torch
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
# # 加载YOLOv8模型
model = YOLO(r'runs\detect\train14\weights\best.pt').to("cuda:0")
#model = YOLO(r'yolov8x.pt').to("cuda:0")
results = model.predict(r'frame_279.jpg')  # predict on an image
print(results[0].boxes)
# # 在帧上展示结果
# annotated_frame = results[0].plot()
# # 展示带注释的帧
# #cv2.imshow("YOLOv8 Tracking", annotated_frame)
# cv2.imwrite(f"runs/111122222.png",annotated_frame)

model.predict(source=r'frame_279.jpg',save=True,show=False,save_crop=True)