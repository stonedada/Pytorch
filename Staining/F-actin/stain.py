import os, sys
import pandas
import tifffile

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from tools import *

if __name__ == '__main__':
    input_imgs = tifffile.imread(f'./UTransform/p147_z006_image.tif').transpose(0, 2, 1)
    target_img = tifffile.imread(f'./UTransform/p147_z006_label.tif').squeeze().transpose(1, 0)
    pre_path = './UTransform/p147_z006_pred_UTransform.tif'
    pre_img = tifffile.imread(pre_path).squeeze().transpose(1, 0)
    output_dir = './UTransform/out_put'
    output_fname = 'p147_z006_v2'

    metrics_df = pandas.read_csv('./metrics_xy.csv')
    metrics = metrics_df.loc[metrics_df['pred_name'].str.contains('im_c001_z006_t000_p147_xy0')]

    save_predicted_images(input_imgs, target_img, pre_img, metrics, output_dir, output_fname)
