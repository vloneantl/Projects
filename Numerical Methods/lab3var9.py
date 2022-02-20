import numpy as np
import matplotlib.pyplot as plt

xtable = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
ytable = np.array([5,6,8,10,12,13,12,10,8,10,8,11,7,9,11,10,9,12,11,6], dtype=float)


def p(x, ind):
    #полином Лагранжа 8-ого порядка
    s = 0
    for k in ind:
        pr=1
        for i in ind:
            if k != i:
                pr *= (x-xtable[i])/(xtable[k]-xtable[i])
        pr*=ytable[k]
        s += pr
    return s

yinterp = []
xinterp = []

#перебор точек
for i in np.arange(1, 5, 0.25):
    f = p(i, (0,1,2,3,4,5,6,7,8))
    print('x =',i, ' y =',f)
    xinterp.append(i)
    yinterp.append(f)

for j in range(5, 15):
    for i in np.arange(j, j+1, 0.25):
        f = p(i, (j-4,j-3,j-2,j-1,j,j+1,j+2,j+3,j+4))
        print('x =', i, ' y =', f)
        xinterp.append(i)
        yinterp.append(f)

for i in np.arange(15, 20.25, 0.25):
    f = p(i, (11,12,13,14,15,16,17,18,19))
    print('x =',i, ' y =', f)
    xinterp.append(i)
    yinterp.append(f)


plt.scatter(xtable, ytable,color='r', label = 'Заданные точки')    #отметим заданные точки на графике
plt.plot(xinterp, yinterp, color='b', label = 'Полином Лагранжа 8-го порядка')  #строим полином на графике
plt.legend()
plt.show()
