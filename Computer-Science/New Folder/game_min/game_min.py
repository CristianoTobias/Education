def computador_escolhe_jogada(n, m):
    for item in range(1, m + 1):
        if (n - item) % (m + 1) == 0:
            if(item > 1):
                print(f"Computador tirou {item} peças")
            else:
                print(f"Computador tirou {item} peça")
            return item
    print(f"Computador tirou {m} peças")
    return m


def usuario_escolhe_jogada(n, m):
    x = input("Quantas peças voce quer tirar? ").strip()
    while not x.isnumeric() or int(n) <= 0 or int(x) > m:
        x = input("Oops! Jogada inválida! Tente de novo. ")
    if(int(x) > 1):
        print(f"\nVocê tirou {x} peças")
    else:
        print(f"\nVocê tirou {x} peça")
    return int(x)


def partida():
    n = input("Quantas peças? ").strip()
    while not n.isnumeric() or int(n) <= 0:
        print("Numero inteiro maior que zero: ")
        n = input("Quantas peças? ").strip()
    n = int(n)
    m = input("Limite de peças por jogada? ").strip()
    while not m.isnumeric() or int(m) <= 0 or int(m) > n:
        print("Numero inteiro maior que zero e menor que o número de peças: ")
        m = input("Limite de peças por jogada? ").strip()
    m = int(m)
    if n % (m + 1) == 0:
        print("\nVocê começa!\n")
        while(n >= 0):
            if(n == 0):
                print("Fim do jogo! O computador ganhou!")
                break
            else:
                n -= usuario_escolhe_jogada(n, m)
                if(n == 0):
                    print("Fim do jogo! Você ganhou!")
                    break
                if(n > 0):
                    if(n > 1):
                        print(f"Agora restam {n} peças no tabuleiro.\n")
                    else:
                        print(f"Agora resta apenas uma peça no tabuleiro.\n")

                n -= computador_escolhe_jogada(n, m)
                if(n > 0):
                    if (n > 1):
                        print(f"Agora restam {n} peças no tabuleiro.\n")
                    else:
                        print(f"Agora resta apenas uma peça no tabuleiro.\n")

    else:
        print("\nComputador começa!\n")
        while (n >= 0):
            if (n == 0):
                print("Fim do jogo! O computador ganhou!")
                break
            else:
                n -= computador_escolhe_jogada(n, m)
                if (n > 0):
                    if (n > 1):
                        print(f"Agora restam {n} peças no tabuleiro.\n")
                    else:
                        print(f"Agora resta apenas uma peça no tabuleiro.\n")
                if(n == 0):
                    continue
                n -= usuario_escolhe_jogada(n, m)
                if (n == 0):
                    print("Fim do jogo! Você ganhou!")
                    break
                if (n > 0):
                    if (n > 1):
                        print(f"Agora restam {n} peças no tabuleiro.\n")
                    else:
                        print(f"Agora resta apenas uma peça no tabuleiro.\n")

def start():
    print("Bem vindo ao jogo do MIM!")
    print("1 - Para jogar uma partida isolada")
    print("2 - Para jogar um campeonato")
    escolha = (input("Escolha: ")).strip()
    while escolha not in '12' or len(escolha) > 1:
        escolha = (input("Escolha 1 or 2: "))
    if escolha == '1':
        print("Você escolheu uma partida isolada!\n")
    else:
        print("Você escolheu um campeonato!\n")
    for rodada in range(1, 4):
        if(escolha == '2'):
            print(f"\n**** Rodada {rodada} ****\n")
        partida()
        if(escolha == '1'):
            break;
    if(escolha == '2'):
        print('\n**** Final do campeonato! ****')
        print('\nPlacar: Você 0 X 3 Computador')



start()
