import os
import json
import shutil
from pathlib import Path
def preprocess(set_name):
    img_dir = "./t_images"
    label_dir = "./t_labels"
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(img_dir+"/"+set_name, exist_ok=True)
    os.makedirs(label_dir, exist_ok=True)
    os.makedirs(label_dir+"/"+set_name, exist_ok=True)
    data_dir = "../hw3_data"
    # copy images to images dir
    for file in os.listdir(os.path.join(data_dir, set_name)):
        if file[-4:] == ".png":
            dst = img_dir+"/"+set_name+"/"+file
            src = data_dir+"/"+set_name+"/"+file
            shutil.copyfile(src,dst) 
    # generate txt file
    with open(os.path.join(data_dir, set_name, "_annotations.coco.json"),"r") as f:
        txt_file = json.load(f)
    for file in os.listdir(os.path.join(data_dir, set_name)):
        if file[-4:] != ".png":#annotation file
            continue
        item = next(item for item in txt_file["images"] if item["file_name"].split("/")[-1] == file)
        image_id = item["id"]
        h_img = item["height"]
        w_img = item["width"]
        items = [ anno for anno in txt_file["annotations"] if anno["image_id"] == image_id ]
        path =  label_dir+"/"+set_name+"/"+file[:-4]+".txt"
        with open(path, "w") as f:
            if len(items) == 0:
                print("got you!!!")
                os.remove(Path(img_dir+"/"+set_name+"/"+file))
                os.remove(Path(path))
            for item in items:
                category = int(item["category_id"]) - 1
                xmin = item["bbox"][0]#xmin
                ymin = item["bbox"][1]#ymin
                w = item["bbox"][2]
                h = item["bbox"][3]
                x_center = (xmin + w/2) / w_img
                y_center = (ymin + h/2) / h_img
                w = w / w_img
                h = h / h_img
                f.write("{} {} {} {} {}\n".format(category, x_center, y_center, w, h))
if __name__ == '__main__':
    preprocess("val")
    preprocess("train")
    