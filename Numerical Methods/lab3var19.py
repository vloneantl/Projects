import numpy as np
import matplotlib.pyplot as plt

x_array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
y_array = np.array([5,6,8,10,12,13,12,10,8,10,8,11,7,9,11,10,9,12,11,6], dtype=float)


def p(x, ind):
    '''
    полином Лагранжа 5-ого порядка
    :param x:
    :param indexes: кортеж из 6 индексов точек
    :return:
    '''
    s = 0
    for k in ind:
        pr=1
        for i in ind:
            if k != i:
                pr *= (x-x_array[i])/(x_array[k]-x_array[i])
        pr*=y_array[k]
        s += pr
    return s

yrange = []
xrange = []

#перебор точек
for i in np.arange(1, 3, 0.25):
    #сначала возьмем первые 6 точек для интерполяции на отрезке [1,3)
    f = p(i, (0,1,2,3,4,5))
    print('x =',i, ' y =',f)
    xrange.append(i)
    yrange.append(f)

for j in range(3, 17):
    #перебор точек для интерполяции на отрезке [3,17)
    for i in np.arange(j, j+1, 0.25):
        f = p(i, (j-2,j-1,j,j+1,j+2,j+3))
        print('x =', i, ' y =', f)
        xrange.append(i)
        yrange.append(f)

for i in np.arange(17, 20.25, 0.25):
    #возьмем последние 6 точек для интерполяции на отрезке [17,20]
    f = p(i, (14,15,16,17,18,19))
    print('x =',i, ' y =',f)
    xrange.append(i)
    yrange.append(f)


plt.scatter(x_array,y_array, label = 'Точки')    #отметим заданные точки на графике
plt.plot(xrange,yrange, color='g', label = 'Полином')  #строим полином на графике
plt.legend()
plt.show()
