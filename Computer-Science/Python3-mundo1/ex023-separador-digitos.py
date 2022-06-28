num = int(input("Digite um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"Analisando o numero {num}...")
print(f"Unidades: {u}")
print(f"Dezenas: {d}")
print(f"Centenas: {c}")
print(f"Milhar: {m}")