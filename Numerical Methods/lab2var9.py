import numpy as np
g = 0
h = 0
j = 0
eps = 0.00001
res = [(2,-2,0.1),(4,0,1),(-3,-3,-0.1)]
def f1(x, y, z):
    return -x**2 + 9.21*x*z**3 + 2*y**2 - 5.4289

def f2(x, y, z):
    return -7.3*x**2*y + 3.21*(x**2)*z**2 - 8.7*y**2 - 2.6 - 42.50873

def f3(x, y, z):
    return 3.5*y**3 - 1.3*(x**3)*z**2 - 6.5 + 50.52268

def df1x(x, y, z):
    return -2*x + 9.21*z**3

def df1y(x, y, z):
    return 4 * y

def df1z(x, y, z):
    return 3 * 9.21*x*z**2

def df2x(x, y, z):
    return -7.3*2*x*y + 2 * 3.21*x*z**2

def df2y(x, y, z):
    return -7.3*x**2 - 2 * 8.7*y

def df2z(x, y, z):
    return 2 * 3.21*(x**2)*z

def df3x(x, y, z):
    return -3 * 1.3*(x**2)*z**2

def df3y(x, y, z):
    return 3 * 3.5*y**2

def df3z(x, y, z):
    return -2 * 1.3*(x**3)*z

print('9 Вариант 2 задание')
print('Решить систему нелинейных уравнений методом Ньютона:')
print('-x**2 + 9.21*x*z**3 + 2*y**2 - 5.4289 = 0')
print('-7.3*x**2*y + 3.21*(x**2)*z**2 - 8.7*y**2 - 2.6 - 42.50873 = 0')
print('3.5*y**3 - 1.3*(x**3)*z**2 - 6.5 + 50.52268 = 0')


for x, y, z in res:
    print('='*80)
    print('x ~',x,'y ~',y,'z ~',z, 'Eps =', eps)
    k = 0
    while k==0 or (abs(xr[0])>eps and abs(xr[1])>eps and abs(xr[2])>eps) :
        k += 1
        A = np.matrix([[df1x(x,y,z), df1y(x, y,z), df1z(x,y,z)],
                       [df2x(x,y,z), df2y(x,y,z), df2z(x,y,z)],
                       [df3x(x,y,z), df3y(x,y,z), df3z(x,y,z)]])
        b = np.array([-f1(x,y,z), -f2(x,y,z), -f3(x,y,z)])
        xr = np.linalg.solve(A,b) #решает матричное уравнение Ax=b
        g = xr[0]
        h = xr[1]
        j = xr[2]
        x = x + g
        y = y + h
        z = z + j
        print('Iteration',k,': x =',x,'y =',y,'z =',z)
    print('f1 =', f1(x,y,z))
    print('f2 =', f2(x,y,z))
    print('f3 =', f3(x, y, z))
