import matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

a, b, c, d, e = -12, -18, 5, 10, -30

lim = 20
step = 0.01
step_acr = 0.0000001
line_style = '-'
line_color = 'b'
direct_up = True

def switch_line():
    global line_style
    if line_style == '-':
        line_style = '--'
    else:
        line_style = '-'
    return line_style

def switch_color():
    global line_color
    if line_color == 'b':
        line_color = 'g'
    else:
        line_color = 'b'
    return line_color

def fun(x):
    return a * x ** 4 * np.sin(np.cos(x)) + b * x ** 3 + c * x ** 2 + d * x + e

x = np.arange(-lim, lim, step)

if fun(x[0]) > fun(x[1]):
    direct_up = False
else:
    direct_up = True

x_change = [(-lim, 'lim')]

for i in range(len(x) - 1):
    if fun(x[i]) > 0 and fun(x[i + 1]) < 0 or fun(x[i]) < 0 and fun(x[i + 1]) > 0:
        x_acr = np.arange(x[i], x[i + 1] + step_acr, step_acr)
        for j in range(len(x_acr) - 1):
            if fun(x_acr[j]) > 0 and fun(x_acr[j + 1]) < 0 or fun(x_acr[j]) < 0 and fun(x_acr[j + 1]) > 0:
                x_change.append((x_acr[j], 'zero'))
    if direct_up:
        if fun(x[i]) > fun(x[i + 1]):
            direct_up = False
            if fun(x[i]) > 0:
                x_change.append((x[i], 'dir_down +'))
            else:
                x_change.append((x[i], 'dir_down -'))
    else:
        if fun(x[i]) < fun(x[i + 1]):
            direct_up = True
            if fun(x[i]) > 0:
                x_change.append((x[i], 'dir_up +'))
            else:
                x_change.append((x[i], 'dir_up -'))

x_change.append((lim, 'lim'))

for i in range(len(x_change) - 1):
    local_step = (x_change[i + 1][0] - x_change[i][0]) / 1000000
    cur_x = np.arange(x_change[i][0], x_change[i + 1][0] + local_step, local_step)
    if x_change[i][1] == 'zero':
        p1, = plt.plot(x_change[i][0], fun(x_change[i][0]), 'yo')
        plt.rcParams['lines.linestyle'] = switch_line()
        if x_change[i + 1][1] == 'dir_up -':
            p2, = plt.plot(cur_x, fun(cur_x), line_color)
        elif x_change[i + 1][1] == 'dir_down +':
            p3, = plt.plot(cur_x, fun(cur_x), line_color)
    else:
        if x_change[i][1] != 'lim':
            p4, = plt.plot(x_change[i][0], fun(x_change[i][0]), 'rx')
        if x_change[i][1] == 'dir_down +':
            p5, = plt.plot(cur_x, fun(cur_x), switch_color())
        elif x_change[i][1] == 'dir_down -':
            p6, = plt.plot(cur_x, fun(cur_x), switch_color())
        elif x_change[i][1] == 'dir_up -':
            p7, = plt.plot(cur_x, fun(cur_x), switch_color())


plt.grid()
plt.legend(handles = [p1, p4, p5, p6, p7, p3], labels = ["Корни уравнения", "Экстремумы", 'Убывает больше 0', 'Убывает меньше 0', 'Возрастает меньше 0', 'Возрастает больше 0'])
plt.show()

