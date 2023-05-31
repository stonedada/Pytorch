import tifffile
import numpy as np

if __name__ == '__main__':
    img_Retardance = "./STNet/img_Retardance_t000_p003_z012.tif"
    img_405 = "./STNet/img_405_t000_p003_z012.tif"
    image = tifffile.imread(img_Retardance).transpose(1, 0)
    label = tifffile.imread(img_405).transpose(1, 0)
    tifffile.imwrite('STNet/Retardance.tif', image, dtype=np.uint16)
    tifffile.imwrite('STNet/_405.tif', label, dtype=np.uint16)
