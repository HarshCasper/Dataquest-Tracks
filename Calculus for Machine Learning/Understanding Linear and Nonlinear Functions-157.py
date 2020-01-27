## 1. Why Learn Calculus? ##

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,3,100)
y = -(x ** 2) + 3 * x - 1
plt.plot(x,y)
plt.show()

## 4. Math Behind Slope ##

def slope(x1, x2, y1, y2):
    s = (y2 - y1) / (x2 - x1)
    return s

slope_one = slope(0,4,1,13)
slope_two = slope(5,-1,16,-2)

print(slope_one)
print(slope_two)

## 6. Secant Lines ##

import seaborn
seaborn.set(style='darkgrid')

def draw_secant(x_values):
    x = np.linspace(-20,30,100)
    y = -1*(x**2) + x*3 - 1
    plt.plot(x,y, c = 'blue')
    y_0 = -1*(x_values[0] ** 2) + x_values[0] * 3 - 1
    y_1 = -1*(x_values[1] ** 2) + x_values[1] * 3 - 1
    m = (y_1 - y_0) / (x_values[1] - x_values[0])
    b = y_1 - m * x_values[1]
    y_s = x * m + b
    plt.plot(x, y_s, c = 'red')
    plt.show()
draw_secant([3,5])
draw_secant([3,10])
draw_secant([3,15])