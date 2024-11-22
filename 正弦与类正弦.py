from scipy.interpolate import make_interp_spline
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
# 设置全局字体
rcParams['font.family'] = 'SimHei'
rcParams['axes.unicode_minus'] = False
# 已知波峰波谷坐标
y = np.array([0, np.pi/2, 0, - np.pi/2, 0git ])
x = np.array([0, 1, 2, 3, 4])

# 样条插值
x_smooth = np.linspace(min(x), max(x), 500)
spline = make_interp_spline(x, y)  # 创建样条函数
y_smooth = spline(x_smooth)  # 生成光滑曲线

# 绘图
plt.plot(x_smooth, y_smooth, label="类正弦曲线", color="green")
plt.scatter(x, y, color="red", label="波峰波谷点")  # 标记原始点
plt.title("类正弦函数 (样条插值)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


