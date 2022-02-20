import numpy as np
'''
Метод Ньютона для решения системы нелинейных алгебраических уравнений
1 шаг: Посчитать матрицу Якоби
Формируем матрицу Якоби:
    (df1x(x, y, z)  df1y(x, y, z)   df1z(x, y, z))
A = (df2x(x, y, z)  df2y(x, y, z)   df2z(x, y, z))
    (df3x(x, y, z)  df3y(x, y, z)   df3z(x, y, z))
Формируем вектор свободных членов B:   
    b = np.array([-f1(x,y,z), -f2(x,y,z), -f3(x,y,z)])

2 шаг: Решить матричное уравнение A*Xr=B
    A*Xr=B => находим Xr
    
3 шаг: задать новое приближение X = X + Xr
    x = x + xr[0]
    y = y + xr[1]
    z = z + xr[2]
4 шаг: Сравниваем с eps
'''
eps = 0.0001
res = [(1,-1,1),(-1,-1,1),(6,5,5),(1,-1,1),(1.5,-1,1.2)] # список начальных приближений

#уравнения
def f1(x, y, z):
    return 8.6*z**3 - 7.3*(x**2)*y + 2*z*y**2 - 30.9312

def f2(x, y, z):
    return 2*x**3 - 3.5*y**3 - 10.7 + 1.196

def f3(x, y, z):
    return 9.6*z**3 - 1.3*(x**2)*y**2 - 5.4 - 8.49312

#функции, возвращающие элементы матрицы якоби
def df1x(x, y, z):
    return -2 * 7.3*x*y

def df1y(x, y, z):
    return - 7.3*(x**2) + 2 * 2 * y * z

def df1z(x, y, z):
    return 3 * 8.6*z**2 + 2*y**2

def df2x(x, y, z):
    return 3*2*x**2

def df2y(x, y, z):
    return - 3*3.5*y**2

def df2z(x, y, z):
    return 0

def df3x(x, y, z):
    return  - 2 * 1.3*(x)*y**2

def df3y(x, y, z):
    return  -2 * 1.3*(x**2)*y

def df3z(x, y, z):
    return 3*9.6*z**2

print('19 Вариант 2 задание')
print('Решить систему нелинейных уравнений методом Ньютона:')
print('8.6*z**3 - 7.3*(x**2)*y + 2*z*y**2 - 30.9312 = 0')
print('2*x**3 - 3.5*y**3 - 10.7 + 1.196 = 0')
print('9.6*z**3 - 1.3*(x**2)*y**2 - 5.4 - 8.49312 = 0')


for x, y, z in res:
    print('-'*80)
    print('Начальное приближение:')
    print('x ~',x,'y ~',y,'z ~',z, 'Eps =', eps)
    k = 0
    while k==0 or (abs(xr[0])>eps and abs(xr[1])>eps and abs(xr[2])>eps) :
        k += 1
        A = np.matrix([[df1x(x,y,z), df1y(x, y,z), df1z(x,y,z)],
                       [df2x(x,y,z), df2y(x,y,z), df2z(x,y,z)],
                       [df3x(x,y,z), df3y(x,y,z), df3z(x,y,z)]])
        b = np.array([-f1(x,y,z), -f2(x,y,z), -f3(x,y,z)])
        xr = np.linalg.solve(A,b) # решает матричное уравнение Ax=b
        x = x + xr[0]
        y = y + xr[1]
        z = z + xr[2]
        print('Итерация №', k,': x = ', x,' y = ', y,' z = ',z,sep='')
    print('Подстановка в уравнения')
    print('f1 =', f1(x,y,z))    #должны быть ~ 0
    print('f2 =', f2(x,y,z))    # e-0x в конце обозначает 10^(-x)
    print('f3 =', f3(x, y, z))  #
