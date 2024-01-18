import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取数据
data = pd.read_csv('data/input_Values.csv')
col1_title = 'Distance_(pixels)'
col2_title = 'Gray_Value'
col1_data = data[col1_title]
col2_data = data[col2_title]
x = col1_data.tolist()
y = col2_data.tolist()

# 构建画布
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Input', linewidth=5)

# 显示图例，并设置标签字体大小
plt.legend(fontsize=20)

# plt.title('Plot Values', fontsize=25)
plt.xlabel('Distance (pixels)', fontsize=20)
plt.ylabel('Gray Value', fontsize=20)
dest = './input_2.png'
plt.savefig(dest)

plt.show()
