import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建一个DataFrame，包含五个样本和三个指标
# 1, 3, 4
data_nuclear = pd.DataFrame({
    'sample':
['3DConvCaps',
    '3DUnet',
    'TransUnet',
    '3D-UCaps',
    'Our 3DCapUnet'],

    'R2Score↑': 
[
0.734,
0.733,
0.728,
0.689,
0.755,
],

    'PCC↑': 
[
0.820,
0.849,
0.845,
0.819,
0.864
],

    'SSIM↑': 
[
0.693,
0.734,
0.736,
0.655,
0.766
],
})

data_Envelope = pd.DataFrame({
    'sample':
['3DConvCaps',
    '3DUnet',
    'TransUnet',
    '3D-UCaps',
    'Our 3DCapUnet'],

    'R2Score↑':
[
0.669,
0.720,
0.709,
0.646,
0.747
],

    'PCC↑':
[
0.820,
0.849,
0.845,
0.819,
0.864
],

    'SSIM↑':
[
0.693,
0.734,
0.736,
0.655,
0.766
],
})
data_Dna = pd.DataFrame({
    'sample':
['3DConvCaps',
    '3DUnet',
    'TransUnet',
    '3D-UCaps',
    'Our 3DCapUnet'],

    'R2Score↑':
[
0.411,
0.464,
0.461,
0.392,
0.485
],

    'PCC↑':
[
0.641,
0.688,
0.696,
0.648,
0.705
],

    'SSIM↑':
[
0.490,
0.500,
0.511,
0.435,

0.526
],
})
data_PCC=pd.DataFrame({ 'sample':
["3DConvCaps",
"3DUnet",
"3DTransUnet",
"3D-UCaps",
"Our 3DCellCapUnet "
],

'Nucleoli':
[0.859,0.857,0.857,0.850,0.869,],

'Nuclear Membrane':
[0.820,0.849,0.845,0.819,0.864],
'Mitochondria':
[
0.662,0.696,0.679,0.683,0.699],


'Actin Filament':
[
0.702,0.683,0.705,0.693,0.736],


'DNA+':
[
0.641,0.688,0.696,0.648,0.705,],

            })



data=data_PCC
plt.figure(figsize=(9, 6))
# 设置雷达图的参数
params = {
    'figure.figsize': [6, 6],
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
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
        # 'y',                        # color
        linewidth=1.3,                # line width
        linestyle='solid', 
        label=data['sample'][i],
    )

    ax.fill(angles, values[i], 
        'b', 
        alpha=0.05,
    )

plt.legend( bbox_to_anchor=(0.8, 0.78),fontsize = 14)
# plt.title('Radar Chart of Three Indicators for Five Samples')

# 设置刻度标签的角度和位置
ax.set_rgrids([0.0, 0.2, 0.4,0.5,0.6,0.7,0.8,0.9,1],
    color="grey", 
    size=14,
    angle=90)
plt.ylim(0.4, 0.9)
# plt.yticks([0.6, 0.8, 1.0], ["0.6", "0.8", "1.0"], color="grey", size=16, rotation=0)


plt.show()
plt.savefig("a.jpg")