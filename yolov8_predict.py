# #https://blog.csdn.net/qq_42452134/article/details/135241059
import cv2
from ultralytics import YOLO
import os
import torch
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
# # 加载YOLOv8模型
model = YOLO(r'runs\detect\train14\weights\best.pt').to("cuda:0")
# results = model.predict("runs/detect/track2/630.png")  # predict on an image
# # 在帧上展示结果
# annotated_frame = results[0].plot()
# # 展示带注释的帧
# #cv2.imshow("YOLOv8 Tracking", annotated_frame)
# cv2.imwrite(f"runs/111122222.png",annotated_frame)

# 打开视频文件
video_path = "result/a4.mp4"
cap = cv2.VideoCapture(video_path)

sz = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fps = 30
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

vout_1 = cv2.VideoWriter()
vout_1.open('result/a4_output_v8_p2_noaug.mp4',fourcc,fps,sz,True)


# 循环遍历视频帧
kk = 0
with open("result.txt","w") as f:
    while cap.isOpened():
        # 从视频读取一帧
        success, frame = cap.read()

        if success:
            # 在帧上运行YOLOv8追踪，持续追踪帧间的物体
            results = model.track(frame, persist=True)
            # 输出每次追踪推理结果的boxes，这些参数实际上是和模型直接predict类似的。
            if len(results[0].boxes.data) !=0:
                result_track = torch.cat((torch.zeros(results[0].boxes.cls.shape).unsqueeze(1).to("cpu"), results[0].boxes.xywh.to("cpu"), results[0].boxes.conf.unsqueeze(1).to("cpu")), dim=1)
                for i in range(result_track.shape[0]):
                    line = f"{kk+1},{int(result_track[i][0].item())}, {result_track[i][1].item()}, {result_track[i][2].item()}, {result_track[i][3].item()}, {result_track[i][4].item()}, {result_track[i][5].item()}, 1, -1, -1"
                    f.write(line+"\n")

                # 在帧上展示结果
                annotated_frame = results[0].plot()
                vout_1.write(annotated_frame)
                # 展示带注释的帧
                #cv2.imshow("YOLOv8 Tracking", annotated_frame)
                os.makedirs("runs/detect/track2",exist_ok=True)
                cv2.imwrite(f"runs/detect/track2/{kk}.png",annotated_frame)
            else:
                vout_1.write(frame)
        else:
            # 如果视频结束则退出循环
            break
        kk +=1