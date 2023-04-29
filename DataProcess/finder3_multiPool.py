import multiprocessing
import os
import argparse
import time
from concurrent.futures import ProcessPoolExecutor

import cv2
import numpy as np


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--path',
        type=str,
        help='path to youre  destination directory'
    )
    args = parser.parse_args()
    return args


def finder(im_path):
    im = cv2.imread(im_path, cv2.IMREAD_ANYDEPTH)
    if im is None:
        return im_path


if __name__ == '__main__':
    args = parse_args()
    path = args.path
    record = []
    files = os.listdir(path)
    for i in files:
        im_path = os.path.join(path, i)
        record.append(im_path)

    # 多线程
    start = time.time()
    # p = multiprocessing.Pool(8)
    # res = p.map(finder, record)
    # res = list(res)
    # p.close()
    # p.join()
    # with ProcessPoolExecutor(8) as ex:
    #     # can't use map directly as it works only with single arg functions
    #     res = ex.map(finder, record)
    #     list(res)
    # np.save("../record.npy", np.array(res))
    # print(res)
    # print('length:', len(res))
    end = time.time()
    print(end - start, 's')
