import numpy as np

M = np.matrix([[7.,5.,1.,0.,35.],
               [1.,2.,0.,1.,8.]])
c = np.array([4,5,0,0])

#print(A)
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

def deltak(ck,cb,Ab,ak):
    '''
    метод, который находит симплекс разности
    '''
    Ab = Ab.transpose()
    Ab = np.linalg.inv(Ab)
    res = cb.dot(Ab)
    res = res.dot(ak)
    return ck - res

def matrixForNewBasis(M, n, m, c):
    '''
    По базисным векторам находит значение опорного вектора
    :param M: заданная матрица
    :param n: номер первого базисного вектора
    :param m: номер второго базисного вектора
    :param c: вектор целевой функции
    :return: матрица, содержащая координаты всех базисных векторов
    '''
    A = np.zeros(M.shape[0]*(M.shape[1]-1)).reshape(M.shape[1] - 1, M.shape[0])
    for i in range(M.shape[1] - 1):
        for j in range(M.shape[0]):
            A[i, j] = M[j, i]
    M[0] = M[0] / M[0, n-1]
    M[1] = M[1] / M[1, m-1]
    M[0] = M[0] - M[1]*M[0,m-1]
    M[0] = M[0] / M[0, n - 1]
    M[1] = M[1] - M[0] * M[1, n - 1]
    if M[0,-1] < 0 or M[1,-1] < 0:
        print('пробуйте другие векторы')
        return
    print('Базис | С(базис) | B опор. | А1 | А2 | А3 | А4 ')
    print(n,'   ',c[n-1],'  ', M[0,-1],' ', M[0,0], M[0,1], M[0,2], M[0,3],sep='  ')
    print(m,'   ',c[m-1],'  ', M[1, -1],' ', M[1, 0], M[1, 1], M[1, 2], M[1, 3],sep='  ')
    result = c[n-1] * M[0,-1] + c[m-1] * M[1, -1]
    print('Наибольшее значение функции: ', result)
    if n > m:
        n, m = m, n
    deltas = []
    for i in range(4):
        di = deltak(c[i], np.array([c[n-1],c[m-1]]),A[n-1:m,:],A[i])
        di = floor(di)
        print('   ','d',i,'=',di, sep='',end=' ')
        deltas.append(di)
    print()
    for item in deltas:
        if item > 0:
            print('нелучшее решение')
            return M
    print('лучшее решение')
    return M

def simplexMethod(M,c):
    for i in range(1, M.shape[1]):
        for j in range(1, M.shape[1]):
            if i != j:
                print(i,j)
                try:
                    M2 = M.copy()
                    c2 = c.copy()
                    matrixForNewBasis(M2, i, j, c2)
                except:
                    pass


matrixForNewBasis(M,1,2,c)
M3 = np.matrix([[2.,1.,1.,0.,0.,10],
               [-2.,3.,0.,1.,0.,6],
                [1.,1.,0.,0.,1.,8]])