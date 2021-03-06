import numpy as np
import matplotlib.pyplot as plt
dg = 7#степень
x_array = np.arange(1,21)
y_array = np.array([5,6,8,10,12,13,12,10,8,10,8,11,7,9,11,10,9,12,11,6], dtype=float)

def p(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    return 2 * x * p(x, n-1) - p(x, n-2)


def formMatrixF():
    f = np.zeros((len(x_array),dg+1))
    for i in range(len(x_array)):
        for j in range(dg+1):
            f[i,j] = p(x_array[i], j)
    return f


def apprFunc(x):
    f = 0
    for i in range(dg+1):
        f += p(x, i) * c[i]
    return f

F = formMatrixF()
c = np.linalg.inv(F.transpose() @ F) @ F.transpose() @ y_array #находим вектор коэффицентов

plt.scatter(x_array,y_array, label = 'Заданные точки')
x_axis = np.arange(1,20.25,0.25)
y_axis = []
for x in x_axis:
    y_axis.append(apprFunc(x))

plt.plot(x_axis,apprFunc(x_axis), label=('Полином Чебышева '+str(dg)+'-ой степени'), color='r')
plt.legend()
plt.show()
sumerror = 0
for index in range(len(x_array)):
    print('x =', x_array[index], '  y =', apprFunc(x_array[index]))
    sumerror += (y_array[index]-y_axis[index*4])**2
print('Сумма квадратов отклонений:',sumerror)
