import numpy as np
import matplotlib.pyplot as plt
import itertools

xarr = np.arange(1,21)
yarr = np.array([5,6,8,10,12,13,12,10,8,10,8,11,7,9,11,10,9,12,11,6], dtype=float)

def pl(x, indexes=(0,1,2,3)):
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
    f = pl(i, (0,1,2,3))
    xrange.append(i)
    yrange.append(f)

for j in range(3, 18):
    for i in np.arange(j, j+1, 0.25):
        f = pl(i, (j-1,j,j+1,j+2))
        xrange.append(i)
        yrange.append(f)

for i in np.arange(18, 20.25, 0.25):
    f = pl(i, (16,17,18,19))
    xrange.append(i)
    yrange.append(f)

#4 задание
def p(x, n):
    # полином Лежандра n-ого порядка
    if n == 0:
        return 1
    if n == 1:
        return x
    return (2*n-1) / n * x * p(x, n - 1) - (n-1) / n * p(x, n-2)


def pr(n):
    '''
    коэффициенты при с
    :param n: номер уравнения наименьшей ошибки
    :return:
    '''
    p_vec = []
    b = 0
    for i in range(7):
        sumpr = 0
        for x in xarr:
            sumpr += p(x, i) * p(x, n)
        p_vec.append(sumpr)
    for i in range(len(xarr)):
        b += yarr[i] * p(xarr[i], n)
    return np.array(p_vec), b

A = np.array(pr(0)[0])
#print('A[0] = ',A)
b = np.array(pr(0)[1])

for i in range(1,7):
   A = np.vstack((A, pr(i)[0]))
   b = np.vstack((b, pr(i)[1]))
#print(A)
#print(b)

c = np.linalg.solve(A,b)
#print('c = ',c)
results = []

for x in np.arange(1, 20.25,0.25):
    res = 0
    for i in range(7):
        res+=p(x,i)*c[i]
    #print(x,' ',res)
    results.append(res[0])


plt.plot(np.arange(1,20.25,0.25),results)
plt.scatter(xrange,yrange, color='y', label='Интерполированные точки')
plt.scatter(xarr,yarr, color='r', label='Заданные точки')
plt.legend()
plt.show()

sumerror = 0
for i in range(20):
    print('x=',i+1, ', полученное значение: ',results[i*4],', табличное значение:',yarr[i],sep='')
    sumerror += (results[i*4] - yarr[i])**2
print('Сумма квадратов отклонений:',sumerror)