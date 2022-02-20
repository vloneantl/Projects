import numpy as np
import matplotlib.pyplot as plt
from math import floor

x_known = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
y_known = np.array([5,6,8,10,12,13,12,10,8,10,8,11,7,9,11,10,9,12,11,6], dtype=float)

def fd(indexes):
    '''
    конечная разность 1 порядка
    :return:
    '''
    return y_known[indexes[1]] - y_known[indexes[0]]

def fd2(indexes):
    '''
    конечная разность 2 порядка
    :return:
    '''
    return y_known[indexes[2]] - 2 * y_known[indexes[1]] + y_known[indexes[0]]

def p(x,h, indexes):
    '''
    полином Ньютона
    :param x:
    :param h:
    :param indexes: массив индексов для заданной таблицы
    :return:
    '''
    x0 = x_known[indexes[0]]
    x1 = x_known[indexes[1]]
    y0 = y_known[indexes[0]]
    P = y0 + fd(indexes) * (x - x0) / h + fd2(indexes) * (x-x0) * (x-x1) / (2 * h ** 2)
    return P

ypoints = [] #массивы, содержащие интерполированные точки
xpoints = []

for x in np.arange(1, 18.25, 0.25):
    y = p(x, 1, [floor(x)-1, floor(x), floor(x)+1])
    print('x =',x,' :  y =',y)
    xpoints.append(x)
    ypoints.append(y)

for x in np.arange(18, 20.25, 0.25):
    y = p(x, 1, [17, 18, 19])
    print('x =',x,' :  y =',y)
    xpoints.append(x)
    ypoints.append(y)


plt.scatter(x_known,y_known, label = 'Заданные точки')    #отметим заданные точки на графике
plt.plot(xpoints,ypoints, color='r', label = 'Полином')  #строим полином на графике
plt.legend()
plt.show()
