import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置全局字体
rcParams['font.family'] = 'SimHei'
rcParams['axes.unicode_minus'] = False

# 数据点
x = np.array([0.19, 0.2, 0.21, 0.22, 0.23, 0.26])
y = np.array([1.1906, 1.2388, 1.309, 1.3799, 1.4494, 1.6134])

# 线性拟合
coefficients = np.polyfit(x, y, 1)
linear_fit = np.poly1d(coefficients)

# 计算拟合值
x_fit = np.linspace(min(x), max(x), 100)
y_fit = linear_fit(x_fit)

# 计算R²值
y_pred = linear_fit(x)  # 用拟合函数预测y值
residuals = y - y_pred  # 残差
ss_res = np.sum(residuals**2)  # 残差平方和
ss_tot = np.sum((y - np.mean(y))**2)  # 总平方和
r_squared = 1 - (ss_res / ss_tot)

# 绘图
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='坐标点', zorder=3)
plt.plot(x_fit, y_fit, color='red', label=f'拟合函数: y = {coefficients[0]:.4f}x + {coefficients[1]:.4f}, $R^2 = {r_squared:.4f}$', zorder=2)
plt.title('白色弹簧', fontsize=14)
plt.xlabel('M/kg', fontsize=12)
plt.ylabel('T\u00B2 / s\u00B2', fontsize=12)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--', alpha=0.6)
plt.axvline(0, color='black', linewidth=0.8, linestyle='--', alpha=0.6)
plt.xlim(0, max(x) + 0.05)
plt.ylim(0, max(y) + 0.1)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

print(f"拟合的 R² 值: {r_squared:.4f}")
