import io
import os
import imageio
from PIL.Image import Image
from skimage import img_as_ubyte
def creat_1d_embedding():
     pass

i=1
img=imageio.imread(r"D:\BIPT\ML\Pytorch\DataProcess\testdata\img_568_t000_p059_z021.tif")
save_path=r"D/TEST"
io.imsave(os.path.join(save_path,"%d_predict.png"%i),img_as_ubyte(img))