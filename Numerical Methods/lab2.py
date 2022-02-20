import numpy as np
import matplotlib.pyplot as plt
g = 0
h = 0
eps = 0.00001
res = [(2, 3),(-2.8, -0.5),(-2, 3), (-2.5,-2.5),(2.4, 3)]

def f1(x, y):
    return x**7 - 5*x**2*y**4 + 1510

def f2(x, y):
    return y**5 - 3*(x**4)*y - 105

def df1x(x, y):
    return 7*(x**6) - 10*x*(y**4)

def df1y(x, y):
    return -20 * (x**2) * (y ** 3)

def df2x(x, y):
    return -12*(x**3)*y

def df2y(x, y):
    return 5 * (y ** 4) - 3 * x**4

for x, y in res:
    print('='*80)
    print('x ~ ',x,'y ~',y)
    k = 0
    while k==0 or (abs(xr[0])>eps and abs(xr[1])>eps):
        k += 1
        A = np.matrix([[df1x(x,y), df1y(x, y)],
                       [df2x(x,y), df2y(x,y)]])
        b = np.array([-f1(x,y), -f2(x,y)])
        xr = np.linalg.solve(A,b)
        g = xr[0]
        h = xr[1]
        x = x + g
        y = y + h
        print('Iteration:',k,'x =',x,'y =',y)


from sympy import var, plot_implicit, symbols, Eq
x,y = symbols('x y')
p1 = plot_implicit(Eq(x*y**3, 5))
"""
delta = 0.025
xrange = np.arange(-5.0, 5.0, delta)
yrange = np.arange(-5.0, 5.0, delta)
X, Y = np.meshgrid(xrange, yrange)
F = f1(X, Y)
plt.contour(X, Y, F, [0])
plt.show()
"""