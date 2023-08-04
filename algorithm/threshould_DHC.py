import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 读取数据
data = np.loadtxt('DHC.txt', skiprows=1)

# 对数据按照x的大小进行排序
data = data[np.argsort(data[:, 0])]
print("max x: ",max(data[:, 0]))
print("min x: ",min(data[:, 0]))


def two_piece_func(x, a, b, c, d):
    return np.piecewise(x, [x <= c, x > c], [lambda x: a * x + b, lambda x: d * x + (a * c + b - c * d)])

p0 = [0, 0.7, 1.3, 2] # initial guess for parameters

# 拟合数据
popt, pcov = curve_fit(two_piece_func, data[:, 0], data[:, 1], p0=p0)

a, b, c, d = popt
xt = c
yt = a * c + b

# 输出拟合参数
print('a =', popt[0])
print('b =', popt[1])
print('c =', popt[2])
print('d =', popt[3])
print("xt = ", xt)
print("yt = ", yt)

xfit = data[:, 0]
yfit = two_piece_func(xfit, *popt)

np.savetxt('./linshi/xfit.txt',xfit)
np.savetxt('./linshi/yfit.txt',yfit)

plt.plot(data[:, 0], data[:, 1], "bo", label="data")
plt.plot(xfit, yfit, "r-", label="fit")
plt.legend()
plt.show()