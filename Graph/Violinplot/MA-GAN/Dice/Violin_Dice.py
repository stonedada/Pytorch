import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

# 加载Excel文件
file_path = '../data/metrics.xlsx'  # 替换为你的Excel文件路径
# 指定要读取的工作表名称或索引，例如读取名为'Sheet1'的工作表
sheet_name = 'DC'  # 也可以使用索引，例如0表示第一个工作表
df = pd.read_excel(file_path, sheet_name)

# 读取特定的一行，例如第5行（注意Python是从0开始计数的）
CARE = df.iloc[0]  # 如果你想读取第5行
RCAN = df.iloc[1]
ESRGAN = df.iloc[2]
pix2pix = df.iloc[3]
MAGAN = df.iloc[4]

plt.figure(dpi=500)
# plt.rcParams["font.family"] = "Times New Roman"  #设置字体的格式
plt.rcParams["axes.unicode_minus"] = False  # 处理负号

label = ["CARE", "RCAN", "ESRGAN", "pix2pix", "MA-GAN"]
font_1 = {"size": 14}

sns.violinplot(data=[CARE, RCAN, ESRGAN, pix2pix, MAGAN], inner='box', scale='count')
plt.ylabel("Dice coefficient", font_1)
# plt.ylim(0.00, 1.50)
plt.xticks(ticks=[0, 1, 2, 3, 4], labels=label, fontsize=11)
plt.yticks(fontsize=12)

# 控制横纵坐标的值域
# plt.axis([-1, 5, -1, 1])

pic_save_name = "./Violin_DC.png"
plt.savefig(pic_save_name)
plt.show()
