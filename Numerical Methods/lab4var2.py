import numpy as np
import matplotlib.pyplot as plt
x_array = np.arange(1,21)
y_array = np.array([5,6,8,10,12,13,12,10,8,10,8,11,7,9,11,10,9,12,11,6], dtype=float)


def T(x, d):
    '''
    полином Чебышева степени d
    '''
    if d == 0:
        return 1
    if d == 1:
        return x
    return 2 * x * T(x, d-1) - T(x, d-2)


def predict(x):
    f = 0
    for i in range(7):
        f += T(x, i) * b[i]
    return f


f = np.zeros((len(x_array), 7))
for i in range(len(x_array)):
    for j in range(7):
        f[i, j] = T(x_array[i], j)
b = np.linalg.inv(f.transpose().dot(f))
b = b.dot(f.transpose()).dot(y_array)

for x in np.arange(1, 20.25, 0.25):
    print('x =', x, 'y =', predict(x))
plt.scatter(x_array, y_array, color='k', label='Заданные точки')
plt.plot(np.arange(1, 20.25, 0.25), predict(np.arange(1, 20.25, 0.25)))
plt.legend()
plt.show()

sse = 0
sse = sum((y_array - predict(x_array))**2)
print('Сумма квадратов отклонений:', sse)
