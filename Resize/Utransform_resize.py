from scipy.ndimage import zoom
from tifffile import tifffile

block_path = f"t000 p003 z012 c001_pred.tif"  # 替换为您的块路径

block = tifffile.imread(block_path)

# 缩放到2048
canvas = zoom(block, (1, 2048 / 128, 2048 / 128), order=3)
tifffile.imwrite("Utransform_pred.tif", canvas)
