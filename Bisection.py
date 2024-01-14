#using <Python>
#Define f(x)= 2*x*cos(2*x) - ((x+1)*(x+1))

import math

def f(x):
    # Define your function f(x) here
    return x*2 - 4  # Replace this with your actual function

x1, x2, x3, fx1, fx2, e, E, fx3, x3new = -3, 0, 0, 0, 0, 0.000001, 0, 0, 0
i = 1
x1=-3
x2=0
e=0.000001

def calculate_E(x3new, x):
    return abs((x3new - x) / x3new) if x3new != 0 else 0

while True:
    fx1 = f(x1)
    fx2 = f(x2)
    x3 = (x2 + x1) / 2
    fx3 = f(x3)
    
    print(f"Iteration: {i} x3 = {x3} f(x3) = {fx3}")

    if fx3 * fx1 < 0:
        x1 = x3
        x3new = (x1 + x2) / 2
        E = calculate_E(x3new, x1)
    else:
        x2 = x3
        x3new = (x1 + x2) / 2
        E = calculate_E(x3new, x2)
    
    i += 1

    if E < e:
        break

print(f"Root = {x3}")

retuen= 0,
