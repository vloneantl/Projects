import numpy as np
import matplotlib.pyplot as plt
st = 6  #степень полинома Лежандра

x_arr = np.arange(1,21)
y_arr = np.array([5,6,8,10,12,13,12,10,8,10,8,11,7,9,11,10,9,12,11,6], dtype=float)

def p(x, n):
    # полином Лежандра n-ого порядка
    if n == 0:
        return 1
    if n == 1:
        return x
    return ((2*n-1) / n) * x * p(x, n - 1) - (n-1) / n * p(x, n-2)

def formMatrixF():
    f = np.zeros((len(x_arr),st+1))
    for i in range(len(x_arr)):
        for j in range(st+1):
            f[i,j] = p(x_arr[i], j)
    return f

F = formMatrixF()
c = np.linalg.inv(F.transpose() @ F) @ F.transpose() @ y_arr #находим вектор коэффицентов

results = []
for x in np.arange(1, 20.25,0.25):
    res = 0
    for i in range(st+1):
        res+=p(x,i)*c[i]
    results.append(res)

plt.plot(np.arange(1,20.25,0.25),results, label=('Полином Лежандра '+str(st)+'-ой степени'))
plt.scatter(x_arr,y_arr, color='g', label='Заданные точки')
plt.legend()
plt.show()

sum_err = 0
for i in range(len(x_arr)):
    print('x=',i+1, ', аппроксимированное значение: ',results[i*4],', табличное значение:',y_arr[i],sep='')
    sum_err += (results[i*4] - y_arr[i])**2
print('Сумма квадратов отклонений:',sum_err)