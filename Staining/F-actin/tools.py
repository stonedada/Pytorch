import cv2
import glob
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import natsort
import numpy as np
import os
import sys
from mpl_toolkits.axes_grid1 import make_axes_locatable


def hist_clipping(input_image, min_percentile=2, max_percentile=98):
    """Clips and rescales histogram from min to max intensity percentiles

    rescale_intensity with input check

    :param np.array input_image: input image for intensity normalization
    :param int/float min_percentile: min intensity percentile
    :param int/flaot max_percentile: max intensity percentile
    :return: np.float, intensity clipped and rescaled image
    """

    assert (min_percentile < max_percentile) and max_percentile <= 100
    pmin, pmax = np.percentile(input_image, (min_percentile, max_percentile))
    hist_clipped_image = np.clip(input_image, pmin, pmax)
    return hist_clipped_image


def save_predicted_images(input_imgs,
                          target_img,
                          pred_img,
                          metric,
                          output_dir,
                          output_fname=None,
                          ext='jpg',
                          clip_limits=1,
                          font_size=15):
    """
    Save plots of predicted images to prediction-figures directory.
    - Overlay of target & prediction
    - Plot of input, target, prediction, and overlay of target & prediction

    :param np.ndarray input_imgs: input images [c,y,x]
    :param np.ndarray target_img: target [y,x]
    :param np.ndarray pred_img: output predicted by the model with same shape as input_img
    :param pd.series/None metric: xy similarity metrics between prediction and target
    :param str output_dir: dir to store the output images/mosaics
    :param str output_fname: fname for saving collage
    :param str ext: 3 letter file extension
    :param float clip_limits: top and bottom % of intensity to saturate
    :param int font_size: font size of the image title
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    n_rows = 2
    # n_cols = np.shape(input_imgs)[0] + 1
    n_cols = 2
    fig, ax = plt.subplots(n_rows, n_cols, squeeze=False)
    ax = ax.flatten()
    for axs in ax:
        axs.axis('off')
    fig.set_size_inches((12, 5 * n_rows))
    axis_count = 0
    # add input images to plot
    for c, input_img in enumerate(input_imgs):
        input_imgs[c] = hist_clipping(
            input_img,
            clip_limits,
            100 - clip_limits,
        )
    # for cur_im in input_imgs:
    #     ax[axis_count].imshow(cur_im, cmap='gray')
    #     ax[axis_count].axis('off')
    #     ax[axis_count].set_title('Input', fontsize=font_size)
    #     axis_count += 1
    cur_im = input_imgs[1]
    ax[axis_count].imshow(cur_im, cmap='gray')
    ax[axis_count].axis('off')
    ax[axis_count].set_title('Input', fontsize=font_size)
    axis_count += 1

    # add target image to plot
    cur_target_chan = hist_clipping(
        target_img,
        clip_limits,
        100 - clip_limits,
    )
    ax_target = ax[axis_count].imshow(cur_target_chan, cmap='gray')
    ax[axis_count].axis('off')
    divider = make_axes_locatable(ax[axis_count])
    cax = divider.append_axes('right', size='5%', pad=0.05)
    cbar = plt.colorbar(ax_target, cax=cax, orientation='vertical')
    ax[axis_count].set_title('Target', fontsize=font_size)
    axis_count += 1

    # add prediction to plot
    ax_img = ax[axis_count].imshow(pred_img, cmap='gray')
    ax[axis_count].axis('off')
    divider = make_axes_locatable(ax[axis_count])
    cax = divider.append_axes('right', size='5%', pad=0.05)
    cbar = plt.colorbar(ax_img, cax=cax, orientation='vertical')
    ax[axis_count].set_title('Prediction', fontsize=font_size)
    axis_count += 1

    # add overlay target - prediction
    cur_target_8bit = convert_to_8bit(cur_target_chan)
    cur_prediction_8bit = convert_to_8bit(pred_img)
    cur_target_pred = np.stack([cur_target_8bit, cur_prediction_8bit,
                                cur_target_8bit], axis=2)

    ax[axis_count].imshow(cur_target_pred)
    ax[axis_count].set_title('Overlay', fontsize=font_size)
    axis_count += 1
    # add metrics
    if metric is not None:
        for c, (metric_name, value) in enumerate(zip(list(metric.keys()), metric.values[0][0:-1]), 1):
            plt.figtext(0.5, 0.001 + c * 0.015, metric_name + ": {:.4f}".format(value), ha="center", fontsize=12)

    fname = os.path.join(output_dir, '{}.{}'.format(output_fname, ext))
    fig.savefig(fname, dpi=300, bbox_inches='tight')
    plt.close(fig)
    fname = os.path.join(output_dir, '{}_overlay.{}'.format(output_fname, ext))
    cv2.imwrite(fname, cur_target_pred)
    fname = os.path.join(output_dir, '{}_prediction.{}'.format(output_fname, ext))
    save_subfig(fig, ax[2], fname)


def convert_to_8bit(img):
    """
    Scales, calculates absolute values, and convert the result to 8-bit.
    :param np.array img: image
    :param float alpha: scale factor
    :return np.array img_8bit: image with 8bit values
    """
    img_8bit = cv2.convertScaleAbs(
        img - np.min(img),
        alpha=255 / (np.max(img) - np.min(img) + sys.float_info.epsilon),
    )
    return img_8bit


# 用于单独保存子图的函数
def save_subfig(fig, ax, save_path):
    bbox = ax.get_tightbbox(fig.canvas.get_renderer()).expanded(1.02, 1.02)
    extent = bbox.transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(save_path, bbox_inches=extent)
