#!/usr/bin/env python
# coding: utf-8

# In[323]:


print('Введите eps')
eps = 0.000001


# In[324]:


from math import factorial
from scipy.special import gammainc 
import mpmath 


# In[325]:


print('Введите x')
x = 0


# In[326]:


def isnatural(s):
    s = str(s)
    natural = tuple('0123456789')
    for item in s:
        if item not in natural:
            return False
    return True


# In[327]:


n = 5
x = 7
if n==0:
    print('n=0')
    n=0.0000001
if isnatural(n):
    print('целое')
    gamma=factorial(n-1)
else:
    #gamma = 0
    print('нецелое')
    gamma=1/n
    for i in range(1,1000000):
        gamma*=((1+1/i)**n)/(1+n/i)
    print(i,'  ',g)
i=0
gamma_new=gamma-(-1)**i*x**(n+i)/(factorial(i)*(n+i))
print(i, ': ',gamma,'  ', gamma_new)
if n==0:
    gamma_new=gamma
else:
    while abs(gamma_new-gamma)>eps:
        i+=1
        gamma = gamma_new
        gamma_new-=(-1)**i*x**(n+i)/(factorial(i)*(n+i))
        #gamma_new+=(-1)**i*x**(n+i)/(factorial(i)*(n+i))
        #print(i, ': ',gamma,'  ', gamma_new)
print(i+1,'итераций')
gamma=gamma_new
print(gamma)


# In[328]:


#print(gammainc(n,x))
print(mpmath.gammainc(n,x))#верхняя гамма функция
if n==1:
    print(math.exp(-x))


# In[303]:


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


# In[304]:


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


# In[246]:


1.644773441846


# In[235]:


1.644787734266078-1.644773441846

