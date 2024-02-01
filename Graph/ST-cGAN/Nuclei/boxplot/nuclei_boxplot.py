import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Nuclei Data
ResUNet_f = pd.read_csv('../data/ResUNet.csv')
TransFuse_f = pd.read_csv('../data/TransFuse.csv')
TransUNet_f = pd.read_csv('../data/TransUNet.csv')
UTransform_f = pd.read_csv('../data/U-Transformer.csv')
pix2pixGAN_f = pd.read_csv('../data/pix2pixGAN.csv')
ST_cGAN_f = pd.read_csv('../data/ST-cGAN.csv')

# ssim
ssim_ResUNet_f = ResUNet_f['SSIM']
ssim_TransFuse_f = TransFuse_f['SSIM']
ssim_TransUNet_f = TransUNet_f['SSIM']
ssim_UTransform_f = UTransform_f['SSIM']
ssim_pix2pixGAN_f = pix2pixGAN_f['SSIM']
ssim_ST_cGAN_f = ST_cGAN_f['SSIM']

# psnr
psnr_ResUNet_f = ResUNet_f['psnr']
psnr_TransFuse_f = TransFuse_f['psnr']
psnr_TransUNet_f = TransUNet_f['psnr']
psnr_UTransform_f = UTransform_f['psnr']
psnr_pix2pixGAN_f = pix2pixGAN_f['PSNR']
psnr_ST_cGAN_f = ST_cGAN_f['PSNR']


# Define my data
ssim_nuclei = [ssim_ResUNet_f, ssim_TransFuse_f, ssim_TransUNet_f, ssim_UTransform_f, ssim_pix2pixGAN_f, ssim_ST_cGAN_f]
psnr_nuclei = [psnr_ResUNet_f, psnr_TransFuse_f, psnr_TransUNet_f, psnr_UTransform_f, psnr_pix2pixGAN_f, psnr_ST_cGAN_f]

# ----------单个图-----------
fig, ax1 = plt.subplots(figsize=(12, 6))
font_size = 15
x1 = np.array([1, 9, 17, 25, 33, 41])
x2 = x1 + 1.1

labels = ['ResUNet', 'TransFuse', 'TransUNet', 'U-Transformer', 'Pix2Pix GAN', 'ST-cGAN']

# SSIM Boxplot
a = ax1.boxplot(ssim_nuclei, positions=x1, patch_artist=True, showmeans=True,
                boxprops={"facecolor": "lightgreen",
                          "edgecolor": "grey",
                          "linewidth": 0.5},
                # medianprops={"color": "k", "linewidth": 0.0},
                meanprops={'marker': '+',
                           'markerfacecolor': 'k',
                           'markeredgecolor': 'k',
                           'markersize': 5}
                )

ax1.set_ylabel('SSIM ↑', fontsize=font_size)
ax1.set_ylim(0, 1)

# PSNR Boxplot
ax2 = ax1.twinx()
b = ax2.boxplot(psnr_nuclei, positions=x2, patch_artist=True, showmeans=True,
                boxprops={"facecolor": "lightblue",
                          "edgecolor": "grey",
                          "linewidth": 0.5},

                meanprops={'marker': '+',
                           'markerfacecolor': 'k',
                           'markeredgecolor': 'k',
                           'markersize': 5}
                )

ax2.set_ylabel('PSNR ↑', fontsize=font_size)
ax2.set_ylim(0, 35)

# General settings
plt.grid(axis='y', ls='--', alpha=1)
plt.grid(True)
plt.title('SSIM and PSNR Comparison among Different Models', fontsize=font_size)
# plt.xlabel('Model', fontsize=font_size)
# plt.ylabel('SSIM', fontsize=14)
plt.xticks(x1 + 0.5, labels, fontsize=12)
plt.xlim(0, 45)

# 给箱体添加图例，每类箱线图中取第一个颜色块用于代表图例
plt.legend(handles=[a['boxes'][0], b['boxes'][0]],
           labels=["SSIM", "PSNR", ], fontsize=15)
plt.tight_layout()
plt.savefig('./nuclei_ssim_psnr.png')
plt.show()  # 展示
