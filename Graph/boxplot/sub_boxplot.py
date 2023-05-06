import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# F-actin Data
ResUNet_f = pd.read_csv('../data/F-actin/ResUNet.csv')
TransFuse_f = pd.read_csv('../data/F-actin/TransFuse.csv')
TransUNet_f = pd.read_csv('../data/F-actin/TransUNet.csv')
UTransform_f = pd.read_csv('../data/F-actin/TransUNet.csv')
ssim_ResUNet_f = ResUNet_f['SSIM']
ssim_TransFuse_f = TransFuse_f['SSIM']
ssim_TransUNet_f = TransUNet_f['SSIM']
ssim_UTransform_f = UTransform_f['SSIM']
# nuclei Data
ResUNet_n = pd.read_csv('../data/nuclei/ResUNet.csv')
TransFuse_n = pd.read_csv('../data/nuclei/TransFuse.csv')
TransUNet_n = pd.read_csv('../data/nuclei/TransUNet.csv')
UTransform_n = pd.read_csv('../data/nuclei/TransUNet.csv')
ssim_ResUNet_n = ResUNet_n['SSIM']
ssim_TransFuse_n = TransFuse_n['SSIM']
ssim_TransUNet_n = TransUNet_n['SSIM']
ssim_UTransform_n = UTransform_n['SSIM']

f_actin_data = [ssim_ResUNet_f, ssim_TransUNet_f, ssim_TransFuse_f, ssim_UTransform_f]
nuclei_data = [ssim_ResUNet_n, ssim_TransUNet_n, ssim_TransFuse_n, ssim_UTransform_n]
font_size = 15
# ----------多个子图-----------
figure, axes = plt.subplots(1, 2)  # 得到画板、轴
axes = axes.flatten()
figure.set_size_inches(15, 6)
a = axes[0].boxplot(f_actin_data, patch_artist=True, )  # 描点上色
axes[0].set_title('F-actin', fontsize=font_size)
b = axes[1].boxplot(nuclei_data, patch_artist=True, )  # 描点上色
axes[1].set_title('Nuclei', fontsize=font_size)

# 颜色填充
colors = ['pink', 'lightblue', 'lightgreen']
for bplot in (a, b):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
# 加水平网格线
for ax in axes:
    ax.yaxis.grid(True)  # 在y轴上添加网格线
    ax.xaxis.grid(True)  # 在x轴上添加网格线
    ax.set_xticks([y + 1 for y in range(len(f_actin_data))])  # 指定x轴的轴刻度个数
    ax.set_xlabel('Model')  # 设置x轴名称
    ax.set_ylabel('SSIM')  # 设置y轴名称

plt.setp(axes, xticks=[1, 2, 3, 4], xticklabels=['ResUNet', 'TransFuse', 'TransUNet', 'UTransform'])
plt.savefig('./ssim.png')
plt.show()  # 展示
