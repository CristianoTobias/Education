dias_aluguel = int(input("Quantos dias alugados? "))
km_rodados = float(input("Quando kilometros rodados? "))
print(f"O total a pagar é R${(dias_aluguel * 60) + (km_rodados * 0.15):.2f}!")
