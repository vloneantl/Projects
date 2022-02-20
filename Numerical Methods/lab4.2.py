import numpy as np
import matplotlib.pyplot as plt
degree = 7  #степень полинома Лежандра + 1
#проверять на малых степенях

xarr = np.arange(1,21)
yarr = np.array([5,6,8,10,12,13,12,10,8,10,8,11,7,9,11,10,9,12,11,6], dtype=float)


def p(x, n):
    # полином Лежандра n-ого порядка
    if n == 0:
        return 1
    if n == 1:
        return x
    return ((2*n-1) / n) * x * p(x, n - 1) - (n-1) / n * p(x, n-2)

print(p(5,6))


def pr(n):
    '''
    коэффициенты при с
    p_str вектор коэф при с в строчке с номером n
    из n строчек p_srt получается матрица А
    :param n: номер уравнения наименьшей ошибки
    :return:
    '''
    p_str = []
    b = 0
    for i in range(degree):
        sum_pr = 0
        for x in xarr:
            sum_pr += p(x, i) * p(x, n)
        p_str.append(sum_pr)
    for i in range(len(xarr)):
        b += yarr[i] * p(xarr[i], n)
    return np.array(p_str), b

A = np.array(pr(0)[0])
#print('A[0] = ',A)
b = np.array(pr(0)[1])


for i in range(1,degree):
   A = np.vstack((A, pr(i)[0]))
   b = np.vstack((b, pr(i)[1]))
#print(A)
#print(b)
print(A)
print(b)

c = np.linalg.solve(A.reshape((degree,degree)),np.array([b]).reshape((degree,1)))
#print('c = ',c)
results = []

for x in np.arange(1, 20.25,0.25):
    res = 0
    for i in range(degree):
        res+=p(x,i)*c[i]
    #print(x,' ',res)
    results.append(res[0])


plt.plot(np.arange(1,20.25,0.25),results)
plt.scatter(xarr,yarr, color='r', label='Заданные точки')
plt.legend()
plt.show()

'''
xspace = np.linspace(1,20,1000)
yspace = p(xspace,1)
plt.plot(xspace, yspace)
yspace = p(xspace,2)
plt.plot(xspace, yspace)
yspace = p(xspace,3)
plt.plot(xspace, yspace)
yspace = p(xspace,4)
plt.plot(xspace, yspace)
yspace = p(xspace,5)
plt.plot(xspace, yspace)
yspace = p(xspace,6)
plt.plot(xspace, yspace)
plt.show()
'''

sumerror = 0
print('-'*80)
for i in range(len(xarr)):
    print('x=',i+1, ', полученное значение: ',results[i*4],', табличное значение:',yarr[i],sep='')
    sumerror += (results[i*4] - yarr[i])**2
print('-'*80)
print('Сумма квадратов отклонений:',sumerror)
print(c)