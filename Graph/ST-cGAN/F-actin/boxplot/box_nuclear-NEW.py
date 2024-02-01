import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'

raw =[ [0.252320135,
0.275403902,
0.461974366,
0.531894633,
0.619668506,
0.827450583], [17.50209857, 17.82478176, 19.05781417, 22.32252362, 23.26849139, 31.18779502]]
CNN = [
    [0.385121516,
0.446272467,
0.501974413,
0.686992583,
0.806245174,
0.881642786,
    ],
      [18.12723896,
18.87321169,
20.14364928,
25.36930752,
30.87365263,
32.11562744,
    ]
]

Unet = [
   [
0.50391318,
0.558142769,
0.688383562,
0.762692772,
0.842607408,
0.931175181,


    ],
    [
20.65178749,
22.54955213,
26.0374831,
29.36470768,
31.3839733,
32.90819395,


    ]

   ]
ResUnet = [
    [0.537528368,
0.572860309,
0.709755006,
0.775735082,
0.84806081,
0.946505605,],
    [22.37166965,
22.89885028,
27.68912751,
30.22315272,
31.96034609,
33.39795238,]
]
ResUnet_CBAM = [
    [0.530134894,
0.566993688,
0.710970622,
0.808087883,
0.889196217,
0.950338137,
],
    [22.12466972,
22.69576044,
27.81218738,
30.64917135,
32.1937693,
33.93752624,

            
        ]
]

TransUnet = [
[0.536449088,
0.571660913,
0.707884332,
0.770675114,
0.849657132,
0.938775585,

],
[22.33401984,
22.87675034,
27.22437301,
30.16767458,
31.54746031,
33.19245668,

],
]

pix2pix = [
[0.571668719,
0.638507707,
0.75202584,
0.809437019,
0.890631996,
0.9509139,


],
[23.37337407,
25.71327402,
28.28506044,
30.67476474,
32.21253132,
33.93553203,


],
]

FLP_GAN=[
[0.583,
0.654,
0.751,
0.792,
0.891,
0.948,

 ],
[23.389,
25.724,
28.286,
30.672,
32.263,
33.929,

 ],
]

import matplotlib.pyplot as plt
import numpy as np

# Data preparation
datasets_ssim = [raw[0], CNN[0], Unet[0], ResUnet[0], ResUnet_CBAM[0], TransUnet[0], pix2pix[0], FLP_GAN[0]]
datasets_psnr = [raw[1], CNN[1], Unet[1], ResUnet[1], ResUnet_CBAM[1], TransUnet[1], pix2pix[1], FLP_GAN[1]]
labels = ["raw", "CNN", "Unet", "ResUnet", "ResUnet_CBAM", "TransUnet", "pix2pix", "FLP_GAN"]

# Plot settings
fig, ax1 = plt.subplots(figsize=(15, 8))

# SSIM Boxplot
bp1 = ax1.boxplot(datasets_ssim, positions=np.arange(len(datasets_ssim)), widths=0.35,
                 patch_artist=True, boxprops=dict(facecolor="#ccebc5"), showmeans=True)

ax1.set_ylabel('SSIM ↑', fontsize=15)
ax1.set_ylim(0, 1)

# PSNR Boxplot
ax2 = ax1.twinx()
bp2 = ax2.boxplot(datasets_psnr, positions=np.arange(len(datasets_psnr))+0.4, widths=0.35,
                  patch_artist=True, boxprops=dict(facecolor="#DFF1FF"), showmeans=True)

ax2.set_ylabel('PSNR ↑', fontsize=15)
ax2.set_ylim(0, 35)

# General settings
plt.xticks(np.arange(len(labels)), labels, fontsize=15)
plt.grid(axis='y', ls='--', alpha=1.0)
plt.title('SSIM and PSNR Comparison among Different Models', fontsize=16)
plt.tight_layout()

# Create custom legend
handles = [bp1["boxes"][0], bp2["boxes"][0]]
plt.legend(handles, ["SSIM", "PSNR"], loc='upper left')

plt.show()
