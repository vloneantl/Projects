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


for i in np.arange(1, 20.25, 0.25):
    f = p(i, (2,7,9,16))
    print(i, '-',f)
    xrange.append(i)
    yrange.append(f)

#найдем лучший базис
errors = []
for basis in itertools.combinations(np.arange(1,20), 4):
    error = 0
    for i in np.arange(1, 21):
        f = p(i, basis)
        error += (f - yarr[i-1])**2
    errors.append((error, basis))
print()

print(min(errors, key= lambda x: x[0] ))



plt.plot(xrange,yrange)
plt.show()
