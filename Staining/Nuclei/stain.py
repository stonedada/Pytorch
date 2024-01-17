import os, sys
import pandas
import tifffile
from tools import *

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

if __name__ == '__main__':
    # model_name = 'ResUNet'
    # model_name = 'UTransformer'
    # model_name = 'STNet'
    # model_name = 'TransUNet'
    # model_name = 'ResUNet'
    model_name = 'TransFuse'
    input_imgs = tifffile.imread(f'./STNet/p003_z012_image_STNet.tif')
    target_img = tifffile.imread(f'./STNet/p003_z012_label_STNet.tif').squeeze()
    pre_path = f'./{model_name}/p003_z012_pred_{model_name}.tif'
    pre_img = tifffile.imread(pre_path).squeeze()
    output_dir = f'./{model_name}/out_put'
    output_fname = f'p003_z012_{model_name}'

    # metrics_df = pandas.read_csv('./metrics_xy.csv')
    # metrics = metrics_df.loc[metrics_df['pred_name'].str.contains('im_c001_z012_t000_p003_xy0')]

    save_predicted_images(input_imgs, target_img, pre_img, None, output_dir, output_fname)