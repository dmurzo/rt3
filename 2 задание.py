import math as m

x = float(input())
y = float(input())
if m.sin(x + y) <= -0.5:
    func = m.atan(m.pow((m.fabs(x - y)), 1 / 3)) * (x * m.pow(m.e, y))
elif m.sin(x + y) < 0.5:
    func = 3 * m.log(m.fabs(x * y), 3) - 0.5
elif m.sin(x + y) >= 0.5:
    func = x ** 3 + y ** 1.5
print(func)
