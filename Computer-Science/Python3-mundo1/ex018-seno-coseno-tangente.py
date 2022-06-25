import math
from math import radians, sin, cos, tan
a = float(input('Digite o angulo que você deseja: '))
a = math.radians(a)
print("*" * 55)
print(f"Seno do ângulo {a} é igual a {math.sin(a):.2f}")
print(f"Coseno do ângulo {a} é igual a {math.cos(a):.2f}")
print(f"Tangente do ângulo {a} é igual a {math.tan(a):.2f}")
print("*" * 55)
print(f"Seno do ângulo {a} é igual a {sin(a):.2f}")
print(f"Coseno do ângulo {a} é igual a {cos(a):.2f}")
print(f"Tangente do ângulo {a} é igual a {tan(a):.2f}")
print("*" * 55)
