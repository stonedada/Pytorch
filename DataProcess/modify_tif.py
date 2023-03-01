# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
import os
import numpy as np
import cv2
import tifffile
dir=r"./testdata"


def merge_path(root,base):
    path=os.path.join(root,base)
    return  path

def read_tif(img_path,flag=cv2.IMREAD_ANYDEPTH):
    img=cv2.imread(img_path,-1)
    print("tif :",img.shape)
    return  img

def context(imgs_dir,files):
    img_path_1 = merge_path(imgs_dir, files[0])
    img1 = read_tif(img_path_1)
    img_path_2 = merge_path(imgs_dir, files[1])
    img2 = read_tif(img_path_2)
    # print(img1,type(img1))
    imgs=np.rint((img1+img2)/2)

    return imgs

def run(dir, flag=0):
    files=os.listdir(dir)
    for index, file in  enumerate(files):
        img_path=merge_path(dir,file)
        img=read_tif(img_path)
        if img is None:
            names=[files[index-1],files[index+1]]
            imgs=context(dir,names)
            new_img=imgs.astype(int)
            # cv2.imwrite(img_path,new_img,((int(cv2.IMWRITE_TIFF_RESUNIT), 2,
            #                                                       int(cv2.IMWRITE_TIFF_COMPRESSION), 1,
            #                                                       int(cv2.IMWRITE_TIFF_XDPI), 100,
            #                                                       int(cv2.IMWRITE_TIFF_YDPI), 100)))
            tifffile.imwrite(img_path,new_img)
            flag+=1
            print(new_img)
    return flag

if __name__ == '__main__':

    a=run(dir)
    print(a)