import numpy as np
import matplotlib.pyplot as plt
import itertools
#полином Лагранжа 3 порядка

xarr = np.arange(1,21)
yarr = np.array([5,6,8,10,12,13,12,10,8,10,8,11,7,9,11,10,9,12,11,6], dtype=float)


def p(x, indexes=(0,1,2,3)):
    '''
    :param x: x
    :param indexes: номера базисных элементов
    :return:
    '''
    s = 0
    for k in indexes:
        p=1
        for i in indexes:
            if k != i:
                p *= (x-xarr[i])/(xarr[k]-xarr[i])
        p*=yarr[k]
        s += p
    return s

yrange = []
xrange = []


for i in np.arange(1, 3, 0.25):
    f = p(i, (0,1,2,3))
    print(i, '-',f)
    xrange.append(i)
    yrange.append(f)

for j in range(3, 18):
    for i in np.arange(j, j+1, 0.25):
        f = p(i, (j-1,j,j+1,j+2))
        print(i, '-',f)
        xrange.append(i)
        yrange.append(f)

for i in np.arange(18, 20.25, 0.25):
    f = p(i, (16,17,18,19))
    print(i, '-',f)
    xrange.append(i)
    yrange.append(f)

plt.scatter(xarr,yarr, label = 'Заданные точки')
plt.plot(xrange,yrange)
plt.show()