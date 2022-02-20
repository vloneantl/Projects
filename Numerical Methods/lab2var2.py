import numpy as np

eps = 0.00001
results = [(-4, -1, -2), (-4, 1, -2),(-2,2,2)]  #список начальных приближений


# уравнения
def f1(x, y, z):
    return  x ** 2 -  x * z + x * y ** 2 - 3 - 5


def f2(x, y, z):
    return y * z + 2 * (x ** 3) * y ** 2 + 9*x*z**2 + 175


def f3(x, y, z):
    return x * y * z - 7.5 * (z ** 4) * x ** 3 - 2 - 4852


# частные производные(формируют матрицу Якоби)
def df1x(x, y, z):
    return 2 * x - z + y ** 2


def df1y(x, y, z):
    return  2 * y * x


def df1z(x, y, z):
    return - x


def df2x(x, y, z):
    return 3 * 2 * x ** 2 * y ** 2 + 9 * z ** 2


def df2y(x, y, z):
    return z + 2 * 2 * y * x ** 3


def df2z(x, y, z):
    return y + 9 * 2 * x * z


def df3x(x, y, z):
    return  z * y - 7.5 * 3 * x ** 2 * z ** 4


def df3y(x, y, z):
    return x * z


def df3z(x, y, z):
    return x * y - 7.5 * 4 * z**3 * x**3


print('2 Вариант 2 задание')
print('Решить систему нелинейных уравнений методом Ньютона:')
print('x**2 - x*z + x*y**2 - 3 = 5')
print('y*z + 2*x**3*y**2 + 9*x*z**2 = -175')
print('x*y*z - 7.5*(z**4)*x**3 - 2 = 4852')

for x, y, z in results:
    print('-' * 80)
    print('Начальное приближение:')
    print('x ~', x, 'y ~', y, 'z ~', z, 'Eps =', eps)
    k = 0
    while k == 0 or (abs(xr[0]) > eps and abs(xr[1]) > eps and abs(xr[2]) > eps):
        k += 1
        A = np.matrix([[df1x(x, y, z), df1y(x, y, z), df1z(x, y, z)],
                       [df2x(x, y, z), df2y(x, y, z), df2z(x, y, z)],
                       [df3x(x, y, z), df3y(x, y, z), df3z(x, y, z)]])
        b = np.array([-f1(x, y, z), -f2(x, y, z), -f3(x, y, z)])
        xr = np.linalg.solve(A, b)  #решает матричное уравнение Ax=b
        x = x + xr[0]
        y = y + xr[1]
        z = z + xr[2]
        print('Итерация №', k, ': x = ', x, ' y = ', y, ' z = ', z, sep='')
    print('Проверка:')
    print('Уравнение 1 =', f1(x, y, z))
    print('Уравнение 2 =', f2(x, y, z))
    print('Уравнение 3 =', f3(x, y, z))
