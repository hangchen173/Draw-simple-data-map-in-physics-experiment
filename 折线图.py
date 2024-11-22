import matplotlib.pyplot as plt
from matplotlib import rcParams
# 设置全局字体
rcParams['font.family'] = 'SimHei'
rcParams['axes.unicode_minus'] = False
# 数据
x = [0,1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
y = [0,0.009, 0.011, 0.023, 0.021, 0.024,0.026,0.026,0.026,0.023,0.023,0.025,0.024,0.021,0.023,0.023,0.022,0.023,0.023,0.023,0.023,0.022,0.023]

# 绘制折线图
plt.plot(x, y, marker='.', linestyle='-', color='b', label='数据曲线')

# 添加标题和轴标签
plt.title('每分钟温升热电势的变化', fontsize=16)
plt.xlabel('t/min', fontsize=12)
plt.ylabel('V/mv', fontsize=12)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--', alpha=0.6)
plt.axvline(0, color='black', linewidth=0.8, linestyle='--', alpha=0.6)
plt.xlim(0, max(x) + 0.05)
plt.ylim(0, max(y) + 0.1)
# 显示图例
plt.legend()

# 显示网格
plt.grid(True, linestyle='--', alpha=0.6)

# 展示图形
plt.show()
