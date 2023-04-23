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
            # tifffile.imwrite(f"./label/c001_{i}_image.tif", block)
            np.save(f"./label/c001_{i}_label.npy", block)
            i += 1
    return blocks


if __name__ == '__main__':

    # 加载输入图像
    # image_path = "example.jpg"  # 替换为您的图像路径
    # image = cv2.imread(image_path)

    # load npy file
    c001 = np.load('./input/t000 p003 z012 c001.npy').transpose(2, 1, 0).astype(dtype=np.float32)
    print('c001 :', c001.shape)
    tifffile.imwrite("c001.tif", c001)
    c000 = np.load('./input/t000 p003 z012 c000.npy').transpose(2, 1, 0).astype(dtype=np.float32)
    print('c000 :', c000.shape)
    tifffile.imwrite("c000.tif", c000)
    # 定义块的大小，这里以100x100像素为例
    block_size = (256, 256)
    # 调用划分函数
    blocks = split_image(c000, block_size)

    # 保存划分后的块
    for i, block in enumerate(blocks):
        # cv2.imwrite(f"block_{i + 1}.jpg", block)
        np.save(f'./output/c000_{i + 1}.npy', block)
