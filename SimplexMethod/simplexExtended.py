import numpy as np
import csv

M = np.matrix([[7.,5.,1.,0.,35.],
               [1.,2.,0.,1.,8.]])
c = np.array([4,5,0,0])

def normalize(M,sign, c):
    '''
    приводит систему ограничений к нормальному виду,
    возвращет матрицу M в каноническом виде
    :param M: матрица ограничений, которую нужно нормализовать
    :param c: целевая функция
    :param sign: знак >=(-1) или <=(1) или =(0)
    :return: M в каноническом виде, кортеж из номеров начального базиса, новый вектор целевой функции
    '''
    n = M.shape[0]
    if sign == 1:
        b = M[:, -1].reshape(M.shape[0], 1)
        s = np.eye(n)
        M = np.hstack((M[:,:-1],s,b))
        m = M.shape[1]
        cc = np.concatenate((c, np.zeros(m - 1 - c.shape[0])))
    elif sign == 0:
        m = M.shape[1]
        cc = np.concatenate((c, np.zeros(m - 1 - c.shape[0])))
    elif sign == -1:
        '''
        решаем вспомогательную задачу
        '''
        b = M[:, -1].reshape(M.shape[0], 1)
        s = np.eye(n)
        M = np.hstack((M[:,:-1], -s, b))
        m = M.shape[1]
        s = np.eye(n)
        M = np.hstack((M[:, :-1], s, b))
        cc = np.concatenate((np.zeros(c.shape[0]),np.zeros(n), -np.ones(n)))
    return M, cc, np.arange(len(cc)-n+1,len(cc)+1)

def floor(x):
    '''
    округляет число до 5 знака
    нужно для сравнения
    :param x:
    :return:
    '''
    x *= 100000
    x = round(x)
    return x / 100000

def checkOpt(deltas):
    '''
    Проверяет является ли решение опциональным
    :param deltas: массив дель
    :return: 1 или 0
    '''
    for item in deltas:
        if item > 0:
            return False
    return True

def deltak(ck,cb,Ab,ak):
    '''
    метод, который находит симплекс разности
    '''
    Ab = Ab.transpose()
    Ab = np.linalg.inv(Ab)
    res = cb.dot(Ab)
    res = res.dot(ak)
    return ck - res

def gauss(M, basis):
    '''
    Решает слау методом Гаусса для любой размерности
    :param M: матрица
    :param basis: номера базисных векторов
    :return: диагональная матрица
    '''
    for i in range(M.shape[0]):
        for j in range(i+1,M.shape[0]):
            M[j] = M[j] - M[i]*M[j,basis[i] - 1] / M[i,basis[i] - 1]
    for i in range(M.shape[0]-1,-1,-1):
        for j in range(i-1,-1,-1):
            M[j] = M[j] - M[i]*M[j,basis[i] - 1] / M[i,basis[i] - 1]
    for i in range(M.shape[0]):
        M[i] = M[i] / M[i, basis[i]-1]
    return(M)

def checkSpace(M, delta, k):
    '''
    Проверяет ограничена ли функция на  целевой области или нет
    :param M:
    :param delta:
    :param k:
    :return:
    '''
    if M.shape[0] == 1:
        for i in range(M.shape[1]):
            if M[0,i] > 0:
                return
        if delta > 0:
            print('Целевая функция не ограничена на целевой области')
            print('Смотрите вектор',k)
            return
        else:
            return
    for i in range(M.shape[0]):
        if M[i] > 0:
            return
    if delta > 0:
        print('Целевая функция не ограничена на целевой области')
        print('Смотрите вектор', k)
        return

def matrixForNewBasis(M, basis, c, tsv_output = None):
    '''
    По базисным векторам находит значение опорного вектора
    Система должна быть в каноническом виде
    :param M: заданная матрица
    :param basis: кортеж, содержащий номера базисных элементов
    :param c: вектор целевой функции
    :return: кортеж из вводимого и выводимого элемента из базиса, если решение не оптимальное,
    если оптимальное, метод возвратит результат
    '''
    A = np.zeros(M.shape[0]*(M.shape[1]-1)).reshape(M.shape[1] - 1, M.shape[0])
    for i in range(M.shape[1] - 1):
        for j in range(M.shape[0]):
            A[i, j] = M[j, i]
    M = gauss(M, basis)
    n, m = M.shape
    result = 0
    cb = []
    print('Базис | С(базис) | B опор. |', end=' ')
    for i in range(m-1):
        print('A'+str(i+1),'|',end=' ')
    print()
    print('-'*80)
    for i in range(n):
        print(basis[i], '   ', c[basis[i] - 1], '  ', M[i, -1], ' ', sep='  ', end='      ')
        for j in range(m-1):
            print(M[i,j],end='  ')
        print()
        result = result + c[basis[i]-1] * M[i,-1]
        cb.append(c[basis[i]-1])
    print('-' * 80)
    print('Значение функции: ', result)
    deltas = []
    Ak = []
    for item in basis:
        Ak.append(A[item-1])
    Ak = np.array(Ak)
    for k in range(M.shape[1]-1):
        dk = deltak(c[k], np.array(cb),Ak,A[k])
        dk = floor(dk)
        print('   ','d',k+1,'=',dk, sep='',end=' ')
        deltas.append(dk)
    print()
    M = M.transpose()
    for i in range(M.shape[0]-1):
        checkSpace(M[i], deltas[i], i+1)
    M = M.transpose()

    if checkOpt(deltas):
        print('решение оптимальное')
    else:
        print('решение неоптимальное')
        maxdeltaindex = deltas.index(max(deltas))
        print('введите в базис A',maxdeltaindex+1, sep='', end='')
        findmin = []
        for i in range(M.shape[0]):
            if M[i,maxdeltaindex] > 0:
                findmin.append(M[i,-1]/M[i,maxdeltaindex])
            else:
                findmin.append(999999999)
        print(' вместо A',basis[findmin.index(min(findmin))], sep='')


    #выведем в tsv
    if tsv_output is None:
        return
    upper = ['','']
    upper.append('Целевая функция')
    upper.extend(c)
    tsv_output.writerow(upper)
    head = ['Базис',  'С(базис)', 'B опор.']
    for i in range(m-1):
        head.append('A'+str(i+1))
    tsv_output.writerow(head)
    Xop = np.zeros(c.shape[0])
    for i in range(n):
        row = []
        row.append('A' + str(basis[i]))
        row.append(c[basis[i] - 1])
        row.append(M[i, -1])
        Xop[basis[i]-1] = M[i,-1]
        for j in range(m-1):
            row.append(M[i,j])
        tsv_output.writerow(row)
    bottom = []
    bottom.append('Значение функции =')
    bottom.append(result)
    bottom.append('deltas =')
    bottom.extend(deltas)
    tsv_output.writerow(bottom)
    answer = []
    if checkOpt(deltas):
        answer.append('Решение оптимальное')
    else:
        answer.append('Решение неоптимальное')
        answer.append('введите в базис A'+str(maxdeltaindex+1)+' вместо A'+str(basis[findmin.index(min(findmin))]))
    answer.append('Xoп='+str(Xop))
    tsv_output.writerow(answer)
    tsv_output.writerow('')

    if checkOpt(deltas):
        return result
    return (maxdeltaindex+1, basis[findmin.index(min(findmin))])
M3 = np.matrix([[10.,1.,1.,0.,0.,5],
               [1.,-1.,0.,1.,0.,1],
                [1.,1.,0.,0.,1.,7]])
c3 = np.array([4,1,0,0,0])
"""



ME = np.array([[1.,-3.,1.,0.,0.,6.],
               [1.,1.,0.,1.,0.,9.],
               [-1.,1.,0.,0.,1.,4.]])
ce = np.array([1.,4.,0,0,0])

M2 = np.array([[1.,-1.,1.,0.,0.,0.,0.,5.],
               [1.,2.,0.,-1.,0.,1.,0,10.],
               [2.,-1.,0.,0.,-1.,0.,1.,2.]])

c2 = np.array([0,0,0,0,0,0,-1])

mc = np.array([[2.,1.,-1.,0.,1.,6.],
               [-1.,3.,0.,1.,0.,9.]])
cc = np.array([-2,3,0,0,0])
"""
mc3 = np.array([[1.,-1.,1.,0.,0.,0.,0.,5.],
               [1.,2.,0.,-1.,0.,1.,0.,10.],
               [2.,-1.,0.,0.,-1.,0.,1.,2.]])
cc3 = np.array([1,1,0,0,0,0,0])

#matrixForNewBasis(M3,(2,4,5),c3)
M3 = np.matrix([[10.,1.,1.,5.],
                [1.,-1.,0.,1.],
                [1.,1.,0.,7.]])
c3 = np.array([4,1,0])
#MM, cc, basis = normalize(M3, 1, c3)

#print(matrixForNewBasis(MM,(2,5,6), cc))
#matrixForNewBasis(mc3,(3,2,1), cc3)


def simplexMethod(M, c, sign):
    f_output = open('solution.tsv', 'w', newline='', encoding='UTF-16')
    tsv_output = csv.writer(f_output, delimiter='\t')
    MM, cc, basis = normalize(M,sign, c)
    res = ()
    while True:
        res = matrixForNewBasis(MM,basis, cc, tsv_output)
        if type(res) is not tuple:
            if sign == -1:
                if res != 0 :
                    print('Целевая функция не имеет допустимых значений')
                    answer = []
                    answer.append('Результат вспомогательной задачи равен')
                    answer.append(res)
                    answer.append('Целевая функция не имеет допустимых значений')
                    tsv_output.writerow(answer)
                else:
                    print('Решаем основную задачу, зная базис')
                    c0 = np.concatenate((c, np.zeros(len(cc)-len(c))))
                    b = MM[:,-1:]
                    result = matrixForNewBasis(np.hstack((MM[:,:-MM.shape[0]-1],b)), basis, c0, tsv_output)
                    #result = matrixForNewBasis(np.hstack((MM[:, :-MM.shape[0] - 1], b)), (1,4), c0, tsv_output)
                    answer = []
                    if type(result) is not tuple:
                        answer.append('Результат основной задачи равен')
                        print('Результат основной задачи равен')
                        answer.append(result)
                        tsv_output.writerow(answer)

            f_output.close()
            return res
        for index, value in enumerate(basis):
            if value == res[1]:
                basis[index] = res[0]


M = np.array([[3.,0.,1.,1.,1000],
             [6.,4.,2.,1.,1100],
              [9.,12.,2.,5.,1300]])

c = np.array([9.,7.,2.,6])

simplexMethod(M,c,1)

