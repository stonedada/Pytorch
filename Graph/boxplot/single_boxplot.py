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

# Define my data
all_data = [np.random.normal(0, std, 100) for std in range(1, 4)]
ssim_factin = [ssim_ResUNet_f, ssim_TransFuse_f, ssim_TransUNet_f, ssim_UTransform_f]
ssim_nuclei = [ssim_ResUNet_n, ssim_TransFuse_n, ssim_TransUNet_n, ssim_UTransform_n]

# ResUNet_ssim = [ssim_ResUNet_f, ssim_ResUNet_n]
# ----------单个图-----------
plt.figure(figsize=(12, 6))
font_size = 15
x1 = np.array([1, 9, 17, 25]) + 3.
x2 = x1 + 1.1
plt.title('boxplot', fontsize=font_size)
labels = ['ResUNet', 'TransFuse', 'TransUNet', 'UTransform']
a = plt.boxplot(ssim_factin, positions=x1, patch_artist=True, showmeans=True,
                boxprops={"facecolor": "lightgreen",
                          "edgecolor": "grey",
                          "linewidth": 0.5},
                medianprops={"color": "k", "linewidth": 0.0},
                meanprops={'marker': '+',
                           'markerfacecolor': 'k',
                           'markeredgecolor': 'k',
                           'markersize': 5}
                )
b = plt.boxplot(ssim_nuclei, positions=x2, patch_artist=True, showmeans=True,
                boxprops={"facecolor": "lightblue",
                          "edgecolor": "grey",
                          "linewidth": 0.5},

                meanprops={'marker': '+',
                           'markerfacecolor': 'k',
                           'markeredgecolor': 'k',
                           'markersize': 5}
                )

plt.xticks(x1 + 0.5, labels, fontsize=12)
plt.xlim(0, 35)
plt.ylim(0, 1)

plt.grid(axis='y', ls='--', alpha=1)
plt.grid(True)
plt.xlabel('Model', fontsize=font_size)
plt.ylabel('SSIM', fontsize=14)

# 给箱体添加图例，每类箱线图中取第一个颜色块用于代表图例
plt.legend(handles=[a['boxes'][0], b['boxes'][0]],
           labels=["Nuclei", "F-actin"], fontsize=15)
plt.tight_layout()
plt.savefig('./ssim_boxplot')
plt.show()  # 展示
