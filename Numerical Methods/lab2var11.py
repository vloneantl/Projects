import numpy as np
import matplotlib.pyplot as plt
import math

eps = 0.00001
res = [(1,1)] #начальное приближения

#уравнения
def f1(x, y):
    return math.sin(x) - y - 1.32

def f2(x, y):
    return math.cos(y) - x + 0.85

#частные производные
def df1x(x, y):
    return math.cos(x)

def df1y(x, y):
    return -1

def df2x(x, y):
    return -1

def df2y(x, y):
    return -math.sin(y)

print('11 Вариант 2 задание')
print('Решить систему нелинейных уравнений методом Ньютона:')
print('sin(x) = y + 1.32')
print('cos(y) = x - 0.85')


for x, y in res:
    print('='*80)
    print('x ~',x,'y ~',y,'Eps =', eps)
    k = 0
    while k==0 or (abs(xr[0])>eps and abs(xr[1])>eps):
        k += 1
        A = np.matrix([[df1x(x,y), df1y(x, y)],
                       [df2x(x,y), df2y(x,y)]])
        b = np.array([-f1(x,y), -f2(x,y)])
        xr = np.linalg.solve(A,b)
        x = x + xr[0]
        y = y + xr[1]
        print('Итерация',str(k) + ':',': x =',x,'y =',y)
    print('f1 =',f1(x,y))
    print('f2 =',f2(x,y))
print('='*80)

#построим график
delta = 0.025
xrange = np.arange(-10.0, 10.0, delta)
yrange = np.arange(-10.0, 10.0, delta)
f1 = np.vectorize(f1)
f2 = np.vectorize(f2)
X, Y = np.meshgrid(xrange, yrange)
plt.contour(X, Y, f1(X, Y), [0])
plt.contour(X, Y, f2(X, Y), [0])
plt.show()

