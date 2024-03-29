import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.DataFrame({'sample':
    [
        "PSNR"
    ],
    'CARE':
        [14.7281],
    'RCAN':
        [17.7223],
    'ESRGAN':
        [23.1478],
    'pix2pix':
        [24.4276],
    'MA-GAN':
        [22.4306],
})

plt.figure(figsize=(9, 8))
# 设置雷达图的参数
params = {
    'figure.figsize': [6, 6],
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'font.weight': 'bold'
}
plt.rcParams.update(params)

# 绘制雷达图
categories = list(data.columns[1:])
N = len(categories)
values = data.iloc[:, 1:].values.tolist()
angles = [n / float(N) * 2 * np.pi for n in range(N)]

# values每一行增加第一个数据; angle增加最后一个角度。 使得曲线闭合
_ = [value.append(value[0]) for value in values]
angles += angles[:1]

ax = plt.subplot(111, polar=True)
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
plt.xticks(angles[:-1], categories)
ax.set_rlabel_position(0)

for i in range(len(values)):
    ax.plot(angles, values[i],
            # 'y',     # color
            linewidth=2,  # line width
            linestyle='solid',
            label=data['sample'][i],
            )

    ax.fill(angles, values[i],
            'b',
            alpha=0.1,
            )
plt.legend(bbox_to_anchor=(1.0, 1.1), fontsize=14)
# plt.legend(loc='upper right', edgecolor='blue')
# 设置标题
# plt.title('F-actin')

# 设置刻度标签的角度和位置
ax.set_rgrids([0, 5, 10, 15, 20, 25, 30, 35],
              color="grey",
              size=11,
              angle=90)
plt.ylim(0, 35)
plt.savefig('radar_psnr.png')
plt.show()
