import math
from math import factorial
import mpmath
import numpy as np
eps = 0.001
print('eps =',eps)
print('-'*80)

def isnatural(s):
    s = str(s)
    natural = tuple('0123456789')
    for item in s:
        if item not in natural:
            return False
    return True

def gammaup(n, x):
    if n<=0:
        print('n<=0')
        return None
    if n==1:
        gamma = math.exp(-x)
        return gamma
    if isnatural(n):
        #print('n целое')
        gamma=factorial(n-1)
    else:
        #gamma = 0
        #print('n нецелое')
        '''
        g = 0.57722
        gamma = math.exp(-g * n) / n
        i = 1
        gamma_new = gamma * ((1 + n / i) ** (-1) * math.exp(n / i))
        while i<100000000:
            i += 1
            gamma = gamma_new
            gamma_new *= ((1 + n / i) ** (-1) * math.exp(n / i))
        '''
        gamma = 1 / n
        i = 1
        gamma_new = gamma * ((1 + 1 / i) ** n) / (1 + n / i)
        while abs(gamma - gamma_new) > eps**3:
        #while i!=10000000:
            i += 1
            gamma = gamma_new
            gamma_new *= ((1 + 1 / i) ** n) / (1 + n / i)
    i=0
    #print('Гамма функция для n равна', gamma)
    #print('Проверка для гамма-функции', math.gamma(n))
    gamma_new=gamma-(-1)**i*x**(n+i)/(factorial(i)*(n+i))
    if n==0:
        gamma_new=gamma
    else:
        while abs(gamma_new-gamma)>eps:
            i+=1
            gamma = gamma_new
            gamma_new-=(-1)**i*x**(n+i)/(factorial(i)*(n+i))
            #gamma_new+=(-1)**i*x**(n+i)/(factorial(i)*(n+i))
            #print(i, ': ',gamma,'  ', gamma_new)
    gamma=gamma_new
    #print('Неполная верхняя гамма функция для n=',n,' и x=',x,' равна ',gamma,sep='')
    #print(gammainc(n,x))
    #print('Проверка', mpmath.gammainc(n,x))#верхняя гамма функция
    #print(mpmath.gammainc(n,x)-gamma)

    '''
    #гамма функция по Эйлеру
    eps=0.00001
    gamma=1/n
    i=1
    gamma_new=gamma*((1+1/i)**n)/(1+n/i)
    while abs(gamma-gamma_new)>eps:
        i+=1
        gamma = gamma_new
        gamma_new*=((1+1/i)**n)/(1+n/i)
    print(eps)
    print(i,'  ',gamma)
    
    #гамма функция по Вейерштрассу
    eps=0.00001
    g=0.57722
    gamma=math.exp(-g*n)/n
    i=1
    gamma_new=gamma*((1+n/i)**(-1)*math.exp(n/i))
    while abs(gamma-gamma_new)>eps:
        i+=1
        gamma = gamma_new
        gamma_new*=((1+n/i)**(-1)*math.exp(n/i))
    print(eps)
    print(i,'  ',gamma)
    '''
    return gamma
for x in [0.5,1,1.2,1.8,2,2.5,3.7,4.6]:
    for n in [0.5,1,1.2,1.8,2,2.5,3.7,4.6]:
        #print('Г(', n, ', ',x,')=',gammaup(n,x),'  Проверка',mpmath.gammainc(n,x)-gammaup(n,x), sep='')
        print('Г(', n, ', ',x,')=',gammaup(n,x), sep='')

