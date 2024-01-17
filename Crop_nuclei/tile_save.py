import numpy as np
import cv2
import tifffile


def split_image(image, block_size):
    """
    将图像按照固定大小的块进行划分

    参数：
    - image: 输入图像，可以是numpy数组
    - block_size: 块的大小，形如 (宽, 高)


    返回值：
    - 块的列表，每个块都是一个numpy数组
    """
    height, width = image.shape[1:3]
    block_width, block_height = block_size
    i = 1
    blocks = []
    for y in range(0, height, block_height):
        for x in range(0, width, block_width):
            block = image[:, y:y + block_height, x:x + block_width]
            print('block :', block.shape)
            blocks.append(block)
            np.save(f'./output/npy_512/p012/c000_{i}_p012_z012.npy', block)
            i += 1
    return blocks


if __name__ == '__main__':
    # load nuclei npy file   c000 as label   c002 as image
    c002 = np.load('./input/t000 p012 z012 c002.npy').transpose(2, 1, 0).astype(dtype=np.float32)
    print('c002 :', c002.shape)
    c000 = np.load('./input/t000 p012 z012 c000.npy').transpose(2, 1, 0).astype(dtype=np.float32)
    print('c000 :', c000.shape)
    # 定义块的大小，这里以100x100像素为例
    block_size = (512, 512)
    # 调用划分函数
    # blocks = split_image(c000, block_size)
    # 输出为tif格式
    image = np.load('./input/t000 p012 z012 c002.npy').transpose(2, 0, 1).astype(dtype=np.float16)
    tifffile.imwrite('t000 p012 z012 c002.tif', image)
    label = np.load('./input/t000 p012 z012 c000.npy').transpose(2, 0, 1).astype(dtype=np.float16)
    tifffile.imwrite('t000 p012 z012 c000.tif', label)
