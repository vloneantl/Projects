import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.linalg
import itertools
import scipy.sparse.linalg

xarr = np.arange(1,21)
yarr = np.array([5,6,8,10,12,13,12,10,8,10,8,11,7,9,11,10,9,12,11,6], dtype=float)

st = 20 #полином 6-го порядка
#всего 2*st+1 слагаемых
#4 задание
'''
def p(x, n):
    # полином n-ого порядка
    res = np.exp(2*np.pi*1j*x*n)
    return complex(res)
print(p(4,2))
'''
def p(x, n):
    # полином n-ого порядка
    res = np.exp(2*np.pi*1j*x*n/20)
    return complex(res)

def pr(n):
    '''
    коэффициенты при с
    :param n: номер уравнения наименьшей ошибки
    :return:
    '''
    p_vec = []
    b = 0
    for i in range(st):
        sumpr = 0
        for x in xarr:
            #print(x,i,n,':',p(x, i),p(x, i),sep='  ')
            sumpr += p(x, i) * p(x, n)
        p_vec.append(sumpr)
    for i in range(len(xarr)):
        b += yarr[i] * p(xarr[i], n)
    return np.array(p_vec), b

A = np.array(pr(0)[0])
#print('A[0] = ',A)
b = np.array(pr(0)[1])



for i in range(1,st):
   A = np.vstack((A, pr(i)[0]))
   b = np.vstack((b, pr(i)[1]))
#print(A)
#print(b)
print(A)
print(b)

#c = np.linalg.solve(A.reshape((st,st)),np.array([b]).reshape((st,1)))
c = scipy.sparse.linalg.spsolve(A.reshape((st,st)),np.array([b]).reshape((st,1)))
#print('c = ',c)
results = []

print(c)
print()
for x in np.arange(1, 20.25,0.25):
    res = 0
    for i in np.arange(-st/2, st/2):
        if i<0:
            res+=p(x,i)*c[-i]
        else:
            res += p(x, i) * c[i]
    #print(x,' ',res)
    results.append(res)


plt.plot(np.arange(1,20.25,0.25),results)
plt.scatter(xarr,yarr, color='r', label='Заданные точки')
plt.legend()
plt.show()

sumerror = 0
for i in range(20):
    print('x=',i+1, ', полученное значение: ',results[i*4],', табличное значение:',yarr[i],sep='')
    sumerror += (results[i*4] - yarr[i])**2
print('Сумма квадратов отклонений:',sumerror)
print(st)

