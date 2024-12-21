import os
import shutil
import cv2

"从snmot数据集中挑选含有足球的数据"
base_path = r"D:\mywork\dataset\IKCEST\images\train"
dataset_image_path = "IKCEST/images/train"
dataset_labels_path = "IKCEST/labels/train"
os.makedirs(dataset_image_path, exist_ok=True)
os.makedirs(dataset_labels_path, exist_ok=True)
snmot_list = os.listdir(base_path)
print(snmot_list)
for path in snmot_list:
    new_path = os.path.join(base_path,path)
    gt = os.path.join(new_path,"gt/gt.txt")
    gameinfo = os.path.join(new_path, "gameinfo.ini")
    with open(gameinfo) as f:
        trackletID_ball = [i.split("=")[0].split("_")[-1] for i in  f.readlines() if "ball" in i]
    print(trackletID_ball)
    with open(gt) as f:
        label = f.readlines()
    for trackletID in trackletID_ball:
        label_list = []
        for i in label:
            seq = i.split(",")
            if seq[1] == trackletID:
                image_path = os.path.join(new_path, 'img1/{:06d}.jpg'.format(eval(seq[0]))).replace("\\","/")
                new_image_path = os.path.join(dataset_image_path,path+"_"+os.path.basename(image_path))
                label_path = os.path.join(dataset_labels_path,path+"_"+os.path.basename(image_path).replace(".jpg",".txt"))
                shutil.copy(image_path,new_image_path)
                x, y, w, h = [eval(mt) for mt in seq[2:6]]
                x_center = x + w / 2
                y_center = y + h / 2
                height, width, channels = cv2.imread(image_path).shape
                normalized_x_center = x_center / width
                normalized_y_center = y_center / height
                normalized_width = w / width
                normalized_height = h / height
                with open(label_path,"a") as wf:
                    wf.write(f"{0} {normalized_x_center} {normalized_y_center} {normalized_width} {normalized_height}\n")

