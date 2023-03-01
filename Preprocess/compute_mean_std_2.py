'''
the inputs should contain "img_405" and "img_phase"
/home/yingmuzhi/microDL_2_0/data/origin/img_405_t000_p004_z003.tif
/home/yingmuzhi/microDL_2_0/data/origin/img_phase_t000_p004_z003.tif
/home/yingmuzhi/microDL_2_0/data/origin/data.csv
'''
import os
from PIL import Image
import numpy as np
import pandas as pd
import cv2
import re


def compute(csv_path: str):
    """
    introduce:
        read .csv file in csv_path, and compute std and mean in different channels according to column "dir_name".

    args:
        :param str csv_path: path to read csv file
    
    return:
        void
    """
    mat_channel1 = np.zeros((2048, 2048), dtype=np.uint16)
    mat_channel2 = np.zeros((2048, 2048), dtype=np.uint16)

    df = pd.read_csv(csv_path)
    dir_name = df[ ["dir_name"] ]
    names = dir_name.to_numpy()
    # squeeze(720, 1) -> (720, )
    names = names.squeeze(axis=1)
    names = list(names)

    length_target = 0
    length_signal = 0
    for name in names:
        if "img_405" in name:
            length_target += 1
            img = cv2.imread(name, cv2.IMREAD_UNCHANGED)
            # judge whether 0 or not
            if img.mean():
                pass
            else:
                print("ZERO!!")
            mat_channel1 += img
        if "img_phase" in name:
            length_signal += 1
            img = cv2.imread(name, cv2.IMREAD_UNCHANGED)
            if img.mean():
                pass
            else:
                print("ZERO!!")
            mat_channel2 += img
    # flatten
    mat_channel1 = mat_channel1.flatten()
    mat_channel2 = mat_channel2.flatten()
    # statistic
    mean_target = mat_channel1.mean()       / length_target
    mean_signal = mat_channel2.mean()       / length_signal
    std_target = mat_channel1.std()         / length_target
    std_signal = mat_channel2.std()         / length_signal
    median_target = np.median(mat_channel1) / length_target 
    median_signal = np.median(mat_channel2) / length_signal
    IQR_target = cal_IQR(mat_channel1)      / length_target
    IQR_signal = cal_IQR(mat_channel2)      / length_signal

    print("channel1-img_405  ::\t\tmean is {}, \t\tstd is {}, \t\tmedian is {}, \t\tiqr is {}".format(mean_target, std_target, median_target, IQR_target))
    print("channel2-img_phase::\t\tmean is {}, \t\tstd is {}, \t\tmedian is {}, \t\tiqr is {}".format(mean_signal, std_signal, median_signal, IQR_signal))


def cal_IQR(data):
    Q1 = np.percentile(data, 25, interpolation='midpoint')
    Q3 = np.percentile(data, 75, interpolation='midpoint')
    IQR = Q3 - Q1
    return IQR


# def main():
#     img_channels = 3
#     img_dir = "/home/yingmuzhi/_data/DRIVE/training/images"
#     roi_dir = "/home/yingmuzhi/_data/DRIVE/training/mask"
#     assert os.path.exists(img_dir), f"image dir: '{img_dir}' does not exist."
#     assert os.path.exists(roi_dir), f"roi dir: '{roi_dir}' does not exist."

#     img_name_list = [i for i in os.listdir(img_dir) if i.endswith(".tif")]
#     cumulative_mean = np.zeros(img_channels)
#     cumulative_std = np.zeros(img_channels)
#     for img_name in img_name_list:
#         img_path = os.path.join(img_dir, img_name)
#         ori_path = os.path.join(roi_dir, img_name.replace(".tif", "_mask.gif"))
#         img = np.array(Image.open(img_path)) / 255.
#         roi_img = np.array(Image.open(ori_path).convert('L'))

#         img = img[roi_img == 255]
#         # img = img.reshape(-1, img_channels)
#         cumulative_mean += img.mean(axis=0)
#         cumulative_std += img.std(axis=0)

#     mean = cumulative_mean / len(img_name_list)
#     std = cumulative_std / len(img_name_list)
#     print(f"mean: {mean}")
#     print(f"std: {std}")


if __name__ == '__main__':
    csv_path = "/home/yingmuzhi/microDL_2_0/data/origin/data.csv"
    compute(csv_path)
    """
    channel1-img_405  ::            mean is 60.739484645071485,             std is 51.175069319406944,              median is 54.642857142857146,           iqr is 67.78571428571429
    channel2-img_phase::            mean is 754.7224228382111,              std is 615.0273158631994,               median is 617.3571428571429,            iqr is 1286.1190476190477
    """

