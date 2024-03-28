import matplotlib.pylab as plt
import seaborn as sns
import pandas as pd

pic_save_name = "./Violin.png"

li_1 = [1, 2, 3]
li_2 = [2.5, 5, 10, 8, 4, 5, 9, 9.5]
li_3 = [1.5, 2.5, 3.5, 6.5]

plt.figure(dpi=300)
plt.rcParams["font.family"] = "SimSun"
plt.rcParams["axes.unicode_minus"] = False

label = ["第一个刻度标签", "第二个刻度标签", "第三个刻度标签"]
font_1 = {"size": 14}

sns.violinplot(data=[li_1, li_2, li_3])
plt.xlabel("横坐标标签", font_1)
plt.ylabel("纵坐标标签", font_1)
plt.xticks(ticks=[0, 1, 2], labels=label, fontsize=11)
plt.yticks(fontsize=12)

plt.savefig(pic_save_name)
plt.show()
