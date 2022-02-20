import numpy as np
import matplotlib.pyplot as plt
x_array = np.arange(1,21)
y_array = np.array([5,6,8,10,12,13,12,10,8,10,8,11,7,9,11,10,9,12,11,6])
n = 4 #степень

a_arr = [0] * (n + 1)
b_arr = [0] * (n + 1)
t = [0]*len(x_array)
for i in range(len(x_array)):
    t[i] = (i+1) * 2 * np.pi / len(x_array)
a_arr[0] = sum(y_array) / len(y_array)

for k in range(1, n+1):
    a_arr[k] = 2 / len(x_array) * sum(y_array[i] * np.cos(k * t[i]) for i in range(len(x_array)))
    b_arr[k] = 2 / len(x_array) * sum(y_array[i] * np.sin(k * t[i]) for i in range(len(x_array)))

def p(x, n):
    res = a_arr[0]
    for i in range(1,n+1):
        res += a_arr[i]*np.cos(2*np.pi*i*x/(len(x_array))) + \
               b_arr[i]*np.sin(2*np.pi*i*x/(len(x_array)))
    return res

y_ip = []
x_ip = np.arange(1, 20.25,0.25)

for x in x_ip:
    res = p(x,n)
    y_ip.append(res)
plt.plot(x_ip,y_ip)
plt.scatter(x_array,y_array, color='r', label='Исходные точки')
plt.legend()
plt.show()

sse = 0
for i in range(len(x_array)):
    print('x=',i+1, ', полученное значение: ',y_ip[i*4],', табличное значение:',y_array[i],sep='')
    sse += (y_ip[i*4] - y_array[i])**2
print('Сумма квадратов отклонений:', sse)