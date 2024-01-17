import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# 读取数据
data = pd.read_csv('Values.csv')
col1_title = 'Distance_(pixels)'
col2_title = 'Gray_Value'
col1_data = data[col1_title]
col2_data = data[col2_title]
x = col1_data.tolist()
y = col2_data.tolist()

# 构建画布
plt.figure(figsize=(9, 5))
plt.plot(x, y, label='Input')

plt.legend()

plt.title('Plot Values')
plt.xlabel(col1_title)
plt.ylabel(col2_title)
dest = './input.png'
plt.savefig(dest)

plt.show()
