import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return 10.5*x**5 + 3.12*x**4 - 6.25*x**3 + 2*x - 26.7

x0 = 0
eps = 0.0001
x = 1
n = 0
print('-'*70)
while abs(x-x0) > eps:
    n += 1
    x , x0 = x - (x - x0) * (f(x)) / (f(x) - f(x0)), x
    print('Iteration:', n, 'x =', x, ' f(x) =', f(x))
print('-'*70)
