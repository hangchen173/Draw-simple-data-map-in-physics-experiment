import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline  # 插值方法
from matplotlib import rcParams
# 设置全局字体
rcParams['font.family'] = 'SimHei'
rcParams['axes.unicode_minus'] = False
# 原始数据
x = np.array([0,1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])
y = np.array([0,0.009, 0.011, 0.023, 0.021, 0.024,0.026,0.026,0.026,0.023,0.023,0.025,0.024,0.021,0.023,0.023,0.022,0.023,0.023,0.023,0.023,0.022,0.023])

# 生成平滑曲线
x_new = np.linspace(x.min(), x.max(), 300)
spl = make_interp_spline(x, y, k=3)  # 使用三次样条插值
y_smooth = spl(x_new)

# 绘图
plt.figure(figsize=(8, 5))
plt.plot(x_new, y_smooth, color="blue")
plt.scatter(x, y, color="red", label="原始数据点")  # 原始数据点
plt.axhline(0, color='black', linewidth=0.8, linestyle='--', alpha=0.6)
plt.axvline(0, color='black', linewidth=0.8, linestyle='--', alpha=0.6)
plt.xlim(0, max(x) + 0.05)
plt.ylim(0, max(y) + 0.1)
plt.xlabel("V/mv")
plt.ylabel("t/min")
plt.title("每分钟温升热电势")
plt.legend()
plt.grid()
plt.show()
