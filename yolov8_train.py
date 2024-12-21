import sys
sys.path.append("ultralytics")
from ultralytics import YOLO
import os
os.system("wandb offline")
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
model = YOLO('yolov8_config/yolov8-p2.yaml').load("yolov8x.pt")
results = model.train(data="yolov8_config/SNMOT.yaml", epochs=40, device='0',
                      batch=4,save=True, resume=True,amp=False,workers=0)  # 断点恢复训练模型