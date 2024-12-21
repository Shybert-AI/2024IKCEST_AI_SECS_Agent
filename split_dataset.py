from glob import iglob
import os
import shutil
import random
dataset_image_path = "IKCEST/images/train"
dataset_labels_path = "IKCEST/labels/train"

dev_dataset_image_path = "IKCEST/images/dev"
dev_dataset_labels_path = "IKCEST/labels/dev"
os.makedirs(dev_dataset_image_path, exist_ok=True)
os.makedirs(dev_dataset_labels_path, exist_ok=True)

imageset = list(iglob(os.path.join(dataset_image_path,"*.jpg"),recursive=True))
print(len(imageset))
test_index = random.sample(list(range(len(imageset))),int(0.2*len(imageset)))
print(len(test_index))
for index in test_index:
    new_image = os.path.join(dev_dataset_image_path,os.path.basename(imageset[index]))
    new_label = os.path.join(dev_dataset_labels_path, os.path.basename(imageset[index]).replace(".jpg",".txt"))
    shutil.move(imageset[index],new_image)
    shutil.move(imageset[index].replace(".jpg",".txt").replace("images","labels"), new_label)


from glob import iglob
import os
base = "IKCEST"

train = ["train","dev"]
for i in train:
    base_path = os.path.join(base,"images",i)
    image_list = list(iglob(os.path.join(base_path,"*.jpg"),recursive=True))
    with open(base + "/" + i + ".txt", "w") as fm:
        for file_ in image_list:
            fm.write("./"+file_.replace("IKCEST","").replace("\\","/")+"\n")