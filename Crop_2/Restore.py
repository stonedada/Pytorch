import cv2
import numpy as np
import tifffile


def combine_blocks(blocks, original_size):
    """
    将块重新组合成原图像

    参数：
    - blocks: 划分后的块列表，每个块是一个numpy数组
    - original_size: 原图像的尺寸，形如 (宽, 高)

    返回值：
    - 组合后的原图像，一个numpy数组
    """
    original_width, original_height = original_size
    # block_width, block_height = blocks[0].shape[:2]
    block_width, block_height = block_size
    rows = original_height // block_height
    cols = original_width // block_width

    # 创建一个空白的画布，用于组合块
    canvas = np.zeros((original_height, original_width, 3), dtype=np.float32)

    # 将块逐行逐列地组合到画布上
    for i, block in enumerate(blocks):
        row = i // rows
        col = i % cols
        y = row * block_height
        x = col * block_width
        canvas[y:y + block_height, x:x + block_width] = block

    return canvas


# 定义块的大小，这里以100x100像素为例
block_size = (256, 256)
# 获取原图像的尺寸
original_size = [2048, 2048]
# 加载划分后的块
original_width, original_height = original_size
block_width, block_height = block_size
rows = original_height // block_height
cols = original_width // block_width
# 创建一个空白的画布，用于组合块
canvas = np.zeros((3, original_height, original_width), dtype=np.float16)
for i in range(1, 65):  # 假设有64个块
    block_path = f"./image/c001_{i}_image.tif"  # 替换为您的块路径
    block = tifffile.imread(block_path)
    # block = np.load(f'./output/c001_{i}.npy')
    # 将块逐行逐列地组合到画布上
    row = (i - 1) // rows
    col = (i - 1) % cols
    y = row * block_height
    x = col * block_width
    canvas[:, y:y + block_height, x:x + block_width] = block

# 调用组合函数
# combined_image = combine_blocks(blocks, original_size)

# 保存组合后的原图像
tifffile.imwrite("image.tif", canvas)
