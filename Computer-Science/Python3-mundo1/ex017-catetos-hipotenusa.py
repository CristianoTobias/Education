import math
from math import hypot
b = float(input("digite o cateto oposto: "))
c = float(input("Digite o cateto adjacente: "))

a = (b**2 + c**2) ** 0.5

print(f"A hipotenusa vais medir {a:.2f}")
print(f"A hipotenusa vais medir {math.hypot(c, b):.2f}")
print(f"A hipotenusa vais medir {hypot(c, b):.2f}")

