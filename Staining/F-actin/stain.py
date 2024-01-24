import os, sys
import pandas
import tifffile
from tools import *

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

if __name__ == '__main__':
    # model_name = 'ResUNet'
    # model_name = 'UTransform'
    # model_name = 'STNet'
    model_name = 'Pix2PixGAN'
    input_imgs = tifffile.imread(f'./UTransform/p003_z012_image.tif').transpose(0, 2, 1)
    target_img = tifffile.imread(f'./UTransform/p003_z012_label.tif').squeeze().transpose(1, 0)
    pre_path = f'./{model_name}/p003_z012_pred_{model_name}.tif'
    pre_img = tifffile.imread(pre_path).squeeze() #.transpose(1, 0)
    output_dir = f'./{model_name}/out_put'
    output_fname = f'p003_z012_{model_name}'

    # metrics_df = pandas.read_csv('./metrics_xy.csv')
    # metrics = metrics_df.loc[metrics_df['pred_name'].str.contains('im_c001_z012_t000_p003_xy0')]

    save_predicted_images(input_imgs, target_img, pre_img, None, output_dir, output_fname)
