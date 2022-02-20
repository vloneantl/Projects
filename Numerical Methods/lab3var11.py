import numpy as np
import matplotlib.pyplot as plt

x_array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
y_array = np.array([5,6,8,10,12,13,12,10,8,10,8,11,7,9,11,10,9,12,11,6])


def p(x, indexes):
    '''
    полином Лагранжа 4-ого порядка
    '''
    sumpr = 0
    for k in indexes:
        pr = 1
        for index in indexes:
            if k != index:
                pr *= (x-x_array[index])/(x_array[k]-x_array[index])
        pr *= y_array[k]
        sumpr += pr
    return sumpr


def ipFunc(x):
    if x >= 1 and x <= 3:
        f = p(x, (0,1,2,3,4))
        return f
    if x <= 20 and x >= 17:
        # возьмем последние 5 точек для интерполяции на отрезке [17,20]
        f = p(x, (15, 16, 17, 18, 19))
        return f
    #перебор точек для интерполяции на отрезке [3,17)
    j = int(np.floor(x))
    f = p(x, (j-2,j-1,j,j+1,j+2))
    return f

plt.scatter(x_array,y_array, label = 'Заданные точки')
x_axis = np.arange(1,20.25,0.25)
y_axis = []
for x in x_axis:
    y_axis.append(ipFunc(x))
    print('x =', x, '  y =', ipFunc(x))

plt.plot(x_axis, y_axis, color='r', label='Полином Лагранжа')
plt.legend()
plt.show()
