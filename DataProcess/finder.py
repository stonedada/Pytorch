import os
import argparse
import cv2
import numpy as np
def parse_args():
    """Parse command line arguments

    In python namespaces are implemented as dictionaries
    :return: namespace containing the arguments passed.
    """
    parser=argparse.ArgumentParser()
    parser.add_argument(
        '--path',
        type=str,
        help='path to youre  destination directory'
    )
    args=parser.parse_args()
    return args

def finder(path):
    record = []
    files=os.listdir(path)
    for i  in files[2:]:
        next_path=os.path.join(path,i)
        next_files=os.listdir(next_path)
        for j in next_files:
            next_next_path = os.path.join(next_path, j)
            next_next_files=os.listdir(next_next_path)
            for k in next_next_files:
                im_path=os.path.join(next_next_path,k)
                im=cv2.imread(im_path,cv2.IMREAD_ANYDEPTH)
                if im is None:
                    record.append(im_path)
    return record

if __name__ == '__main__':
    args=parse_args()
    list=finder(args.path)
    a=np.array(list)
    np.save("record.npy", a)
    print(list)
    print(len(list))