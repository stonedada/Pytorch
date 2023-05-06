# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
from  finder import *
from  modify_tif import *



if __name__ == '__main__':
    #args=parse_args()
    # dir=r'D:\Data\Medical Imaging\p5-p12\data'
    dir = r'C:\Users\hp\Desktop\img'
    num=run(dir)
    print("have processed {} iamges".format(num))