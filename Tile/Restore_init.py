import cv2
import numpy as np

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
    block_width, block_height = blocks[0].shape[:2]
    rows = original_height // block_height
    cols = original_width // block_width

    # 创建一个空白的画布，用于组合块
    canvas = np.zeros((original_height, original_width, 3), dtype=np.uint8)

    # 将块逐行逐列地组合到画布上
    for i, block in enumerate(blocks):
        row = i // cols
        col = i % cols
        y = row * block_height
        x = col * block_width
        canvas[y:y + block_height, x:x + block_width] = block

    return canvas

# 定义块的大小，这里以100x100像素为例
block_size = (100, 100)

# 加载划分后的块
blocks = []
for i in range(1, 10):  # 假设有9个块
    block_path = f"block_{i}.jpg"  # 替换为您的块路径
    block = cv2.imread(block_path)
    blocks.append(block)

# 获取原图像的尺寸
original_path = "example.jpg"  # 替换为您的图像路径
original_image = cv2.imread(original_path)
original_size = original_image.shape[:2]

# 调用组合函数
combined_image = combine_blocks(blocks, original_size)

# 保存组合后的原图像
cv2.imwrite("combined.jpg", combined_image)
