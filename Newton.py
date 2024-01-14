#using <Python>
#define f(x) 2*x*cos(2*x) - ((x+1)*(x+1))
#define g(x) -2*(2*x*sin(2*x)-cos(2*x))-2*(x+1)

import math

def f(x):
    return 2 * x * math.cos(2 * x) - ((x + 1) * (x + 1))

def g(x):
    return -2 * (2 * x * math.sin(2 * x) - math.cos(2 * x)) - 2 * (x + 1)

x1, x0, f0, g0, e, E, f1, xold = 0, -3, 0, 0, 0.000001, 0, 0, 0
i = 1

while True:
    f0 = f(x0)
    g0 = g(x0)
    x1 = x0 - (f0 / g0)
    xold = x0
    x0 = x1
    f1 = f(x1)

    print(f"Iteration: {i} x = {x1} f(x) = {f1}")

    E = abs((x0 - xold) / x0)
    i += 1

    if E < e:
        break

print(f"Root = {x1}")

retuen= 0,

