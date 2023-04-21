import numpy as np
import cv2


def split_image(image, block_size):
    """
    将图像按照固定大小的块进行划分

    参数：
    - image: 输入图像，可以是numpy数组
    - block_size: 块的大小，形如 (宽, 高)

    返回值：
    - 块的列表，每个块都是一个numpy数组
    """
    height, width = image.shape[:2]
    block_width, block_height = block_size

    blocks = []
    for y in range(0, height, block_height):
        for x in range(0, width, block_width):
            block = image[y:y + block_height, x:x + block_width, :]
            blocks.append(block)

    return blocks


if __name__ == '__main__':

    # 加载输入图像
    # image_path = "example.jpg"  # 替换为您的图像路径
    # image = cv2.imread(image_path)

    # load npy file
    c001 = np.load('./input/t000 p003 z012 c001.npy')
    print(c001.shape)
    c000 = np.load('./input/t000 p003 z012 c000.npy')
    print(c000.shape)
    # 定义块的大小，这里以100x100像素为例
    block_size = (256, 256)
    # 调用划分函数
    blocks = split_image(c000, block_size)

    # 保存划分后的块
    for i, block in enumerate(blocks):
        # cv2.imwrite(f"block_{i + 1}.jpg", block)
        np.save(f'./output/c000_{i+1}.npy',block)
