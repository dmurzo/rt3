import math as m


def func(x, y):
    if x + y <= 4:
        f = (m.sin(x * (m.e ** (0.1 * y)))) ** (1 / 3)
    elif x + y > 2:
        f = abs(m.log(x + y, 2))
    return f


x = 1
while x <= 2.5:
    y = 1
    while y <= 4:
        print(func(x, y))
        y += 1
    x += 0.5
