import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.linalg
import itertools
import scipy.sparse.linalg

x_known = np.arange(1,21)
y_known = np.array([5,6,8,10,12,13,12,10,8,10,8,11,7,9,11,10,9,12,11,6])
st = 6 #полином 6-го порядка

#всего 2*st+1 слагаемых
'''
def p(x, n):
    # полином n-ого порядка
    res = np.exp(2*np.pi*1j*x*n)
    return complex(res)
print(p(4,2))
'''
def p(x, n):
    # n-ое слагаемое в тригонометрическом ряду
    t = 2 * np.pi * (x)/(20)
    if n==0:
        return x
    return (math.cos(n*t), math.sin(n*t))

def pr(n):
    '''
    коэффициенты при с
    :param n: номер уравнения наименьшей ошибки
    :return:
    '''
    p_vec = []
    b = 0
    for i in range(st):
        sumpr = 1
        for x in x_known:
            #print(x,i,n,':',p(x, i),p(x, i),sep='  ')
            if i==0 and n==0:
                sumpr += p(x, i) * p(x, n) + p(x, i) * p(x, n)
            elif i == 0:
                sumpr += p(x, i) * p(x, n)[0] + p(x, i) * p(x, n)[1]
            elif n == 0:
                sumpr += p(x, i)[0] * p(x, n) + p(x, i)[0] * p(x, n)
            else:
                sumpr += p(x, i)[0] * p(x, n)[0] + p(x, i)[1] * p(x, n)[1]
        p_vec.append(sumpr)
    for i in range(len(x_known)):
        if n == 0:
            b += y_known[i] * p(x_known[i], n)+y_known[i] * p(x_known[i], n)
        else:
            b += y_known[i] * p(x_known[i], n)[0]+y_known[i] * p(x_known[i], n)[1]
    return np.array(p_vec), b


def formAandB(st):
    '''
    нужно чтобы сформировать матрицу А и вектор В для решения матричного
    уравнения, где находим вектор с
    :param st:
    :return:
    '''
    A = np.array(pr(0)[0])
    #print('A[0] = ',A)
    b = np.array(pr(0)[1])
    for i in range(1,st):
       A = np.vstack((A, pr(i)[0]))
       b = np.vstack((b, pr(i)[1]))
    return A, b

A, b = formAandB(st)
print(A)
print(b)
#c = np.linalg.solve(A.reshape((st,st)),np.array([b]).reshape((st,1)))
c = scipy.sparse.linalg.spsolve(A.reshape((st,st)),np.array([b]).reshape((st,1)))
#решаем матричное уравнение   Ac=b, находим с
y_ip = []
x_ip = np.arange(1, 20.25,0.25)

for x in x_ip:
    res = p(x,0)
    for i in range(1,st):
        res+=p(x,i)[0]*c[i]+p(x,i)[1]*c[i]
    y_ip.append(res)

plt.plot(x_ip,y_ip)
plt.scatter(x_known,y_known, color='g', label='Известные точки')
plt.legend()
plt.show()

sse = 0
for i in range(len(x_known)):
    print('x=',i+1, ', полученное значение: ',y_ip[i*4],', табличное значение:',y_known[i],sep='')
    sse += (y_ip[i*4] - y_known[i])**2
print('Сумма квадратов отклонений:',sse)

