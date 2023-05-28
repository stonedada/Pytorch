import cv2
import numpy as np
import tifffile
from scipy.ndimage import zoom

if __name__ == '__main__':

    # model_name = 'ResUNet'
    model_name = 'UTransform'

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
    # canvas = np.zeros((1, original_height, original_width), dtype=np.float32)
    canvas = np.zeros((1, original_height, original_width), dtype=np.float32)
    for i in range(1, 65):  # 假设有17个块
        block_path = f"./{model_name}/pred_p003/c001_{i}_p003_z012_pred.tif"  # 替换为您的块路径
        # block_path = f'./UTransform/pred_p003/c001_{i}_p147_z006_pred.tif'
        block = tifffile.imread(block_path)
        # 缩放到512 or 256
        # block = zoom(block, (1, 4, 4), order=3)
        block = zoom(block, (1, 2, 2), order=3)
        # 将块逐行逐列地组合到画布上
        row = (i - 1) // rows
        col = (i - 1) % cols
        y = row * block_height
        x = col * block_width
        # canvas[:, y:y + block_height, x:x + block_width] = block
        canvas[:, y:y + block_height, x:x + block_width] = block

    # 保存组合后的原图像
    tifffile.imwrite(f"./{model_name}/p003_z012_pred_UTransform.tif", canvas)
