import numpy as np
import matplotlib.pyplot as plt

x_array = np.arange(1,21)
y_array = np.array([5,6,8,10,12,13,12,10,8,10,8,11,7,9,11,10,9,12,11,6])


def L(x, x_arr, y_arr):
    '''
    полином Лагранжа 5-ого порядка
    '''
    s = 0
    for i in range(len(x_arr)):
        pr = 1
        for j in range(len(x_arr)):
            if i != j:
                pr *= (x-x_arr[j])/(x_arr[i]-x_arr[j])
        pr *= y_arr[i]
        s += pr
    return s


def predict(x):
    if x >= 1 and x <= 3:
        f = L(x, x_array[:6], y_array[:6])
        return f
    if x <= 20 and x >= 17:
        f = L(x, x_array[-6:],y_array[-6:])
        return f
    j = int(np.floor(x))
    f = L(x, x_array[j-3:j+3], y_array[j-3:j+3])
    return f


x_axis = np.arange(1,20.25,0.25)
y_axis = []
for x in x_axis:
    y_axis.append(predict(x))
    print('x =', x, 'y =', predict(x))
plt.scatter(x_array,y_array, label = 'Заданные точки')
plt.plot(x_axis, y_axis, color='r', label='Полином Лагранжа')
plt.legend()
plt.show()