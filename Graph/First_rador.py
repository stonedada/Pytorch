import matplotlib.pyplot as plt
import numpy as np

#  eg1:

# plt.polar(0.25 * np.pi, 20, 'ro', lw=2)
#  eg2:

# theta = np.array([0.25, 0.75, 1, 1.5, 0.25])
# r = [20, 60, 40, 80, 20]
# plt.polar(theta * np.pi, r, 'ro-', lw=2)
# plt.ylim(0, 100)
# plt.show()

# eg3:
plt.rcParams['font.sans-serif'] = ['SimHei']

name = ['语文', '数学', '英语', '物理', '化学']  # 标签
theta = np.linspace(0, 2 * np.pi, len(name), endpoint=False)  # 将圆根据标签的个数等比分
value = np.random.randint(50, 100, size=5)  # 在60-120内，随机取5个数
theta = np.concatenate((theta, [theta[0]]))  # 闭合
value = np.concatenate((value, [value[0]]))  # 闭合

ax = plt.subplot(111, projection='polar')  # 构建图例
ax.plot(theta, value, 'm-', lw=1, alpha=0.75)  # 绘图
ax.fill(theta, value, 'm', alpha=0.75)  # 填充
ax.set_thetagrids(theta * 180 / np.pi, name)  # 替换标签
ax.set_ylim(0, 110)  # 设置极轴的区间
ax.set_theta_zero_location('N')  # 设置极轴方向
ax.set_title('木子李-五维图', fontsize=20)  # 添加图描述
plt.show()
