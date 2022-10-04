import math as m


def func(x):
    f = m.cos(m.e * x) ** 3 + m.sin(abs(x))
    return f


xn, xk, hx = float(input()), float(input()), float(input())
x = xn
while x <= xk:
    print(func(x))
    x += hx
