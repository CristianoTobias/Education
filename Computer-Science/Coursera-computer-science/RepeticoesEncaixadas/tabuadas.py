linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10:
        print(coluna * linha, end="\t")
        coluna = coluna + 1
    print()
    linha = linha + 1
    coluna = 1

x = 1
while x < 3:
    y = 1
    while y < 3:
        print(x*y, end = "\t")
        y = y + 1
    x = x + 1