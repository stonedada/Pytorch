import os
import argparse
import cv2
import numpy as np


def parse_args():
    """Parse command line arguments

    In python namespaces are implemented as dictionaries
    :return: namespace containing the arguments passed.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--path',
        type=str,
        help='path to youre  destination directory'
    )
    args = parser.parse_args()
    return args


def finder(path):
    record = []
    files = os.listdir(path)
    for i in files:
        im_path = os.path.join(path, i)
        im = cv2.imread(im_path, cv2.IMREAD_ANYDEPTH)
        if im is None:
            record.append(im_path)
    return record


if __name__ == '__main__':
    args = parse_args()
    list = finder(args.path)
    a = np.array(list)
    np.save("./record.npy", a)
    print(list)
    print('length:', len(list))
