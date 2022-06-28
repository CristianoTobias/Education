
def min_max(temperaturas):
    print(f"A menor temperatura do mês foi: {minima(temperaturas)}")
    print(f"A maior temperatura do mês foi: {maxima(temperaturas)}")


def minima(temps):
    min = temps[0]
    i = 0
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min

def maxima(temps):
    max = temps[0]
    i = 0
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max


def teste_pontual(temp, valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
        print(f"Valor esperado: {valor_esperado}. Valor calculado: {valor_calculado}")

def teste_pontual2(temp, valor_esperado):
    valor_calculado = maxima(temp)
    if valor_calculado != valor_esperado:
        print(f"Valor esperado: {valor_esperado}. Valor calculado: {valor_calculado}")


def testa_minima():
    print("Inciando os testes...")
    teste_pontual([0], 0)
    teste_pontual([0, 0, 0, 0, 0, 0 , 0], 0)
    teste_pontual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0)
    teste_pontual([30, 27, 25, 26, 29, 22, 32, 33, 24, 26], 22)
    teste_pontual([-12, -15, 0, 20, 30], -15)
    print("Finalizando os testes...")

def testa_maxima():
    print("Inciando os testes...")
    teste_pontual2([0], 0)
    teste_pontual2([0, 0, 0, 0, 0, 0 , 0], 0)
    teste_pontual2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
    teste_pontual2([30, 27, 25, 26, 29, 22, 32, 33, 24, 26], 33)
    teste_pontual2([-12, -15, 0, 20, 30], 30)
    print("Finalizando os testes...")


min_max([30, 27, 25, 26, 29, 22, 32, 33, 24, 26])