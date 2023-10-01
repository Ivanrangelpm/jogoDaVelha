import random

def ImprimeMenuPrincipal():
    print("Bem-vindo ao Jogo da Velha!")
    print("Escolha uma opção:")
    print("1. Jogar contra outro jogador")
    print("2. Jogar contra a máquina")
    escolha = input()
    
    if escolha == "1":
        for rodar in range(3):
            modoJogador()
            print("Pontuação:" )
            print("Jogador X: ", imprimePontuacao['Jogador X'])
            print("Jogador O: ", imprimePontuacao['Jogador O'])
            print("Empate: ", imprimePontuacao['Empate'])
    elif escolha == "2":
        for rodar in range(3):
            modoFacil()
            print("Pontuação:" )
            print("Jogador X: ", imprimePontuacao['Jogador X'])
            print("Jogador O: ", imprimePontuacao['Jogador O'])
            print("Empate: ", imprimePontuacao['Empate'])
    else:
        print("Opção inválida. Digite novamente.")
        ImprimeMenuPrincipal()

imprimePontuacao = {"Jogador X": 0, "Jogador O": 0, "Empate" : 0}

def modoJogador():

    tabuleiro = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]

    vitoria = False

    global imprimePontuacao

    def ImprimirTabuleiro():
        print("\n")
        for linha in tabuleiro:
            print("", " ! ".join(linha))
            if linha != tabuleiro[-1]:
                print("---!---!---")
        print("\n")

    def verificaVencedor(jogador):
        for linha in tabuleiro:
            if all(posicao == jogador for posicao in linha):
                return True
        for coluna in range(3):
            if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
                return True
        if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2-i] == jogador for i in range(3)):
            return True
        return False

    def PosicaoValida():
        while True:
            numero = input()
            try:
                numero = int(numero)
                if numero in range(1, 10):
                    return numero
                else:
                    print("\nNúmero não está no tabuleiro.")
            except ValueError:
                print("\nIsso não é um número. Tente novamente.")
                continue

    def jogadaUsuario(jogador):
        espaco_colocado = PosicaoValida() - 1
        linha = espaco_colocado // 3
        coluna = espaco_colocado % 3
        if tabuleiro[linha][coluna] == "X" or tabuleiro[linha][coluna] == "O":
            print("\nEspaço já ocupado. Tente colocar em outro.")
            jogadaUsuario(jogador)
        else:
            tabuleiro[linha][coluna] = jogador

    jogadas = 0
    while not vitoria:
        ImprimirTabuleiro()
        vitoria = verificaVencedor("O")
        if vitoria:
            print("Jogador O venceu!")
            imprimePontuacao['Jogador O'] += 1
            break

        if jogadas == 9:
            print("O jogo acabou em empate.")
            imprimePontuacao['Empate'] += 1
            break

        print("Jogador X, escolha um espaço.")
        jogadaUsuario("X")
        jogadas += 1

        ImprimirTabuleiro()
        vitoria = verificaVencedor("X")
        if vitoria:
            print("Jogador X venceu!")
            imprimePontuacao['Jogador X'] += 1
            break

        print("Jogador O, escolha um espaço.")
        jogadaUsuario("O")
        jogadas += 1    

def modoFacil():
    tabuleiro = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    vitoria = False

    global imprimePontuacao

    def ImprimirTabuleiro():
        print("\n")
        for linha in tabuleiro:
            print("", " ! ".join(linha))
            if linha != tabuleiro[-1]:
                print("---!---!---")
        print("\n")

    def verificaVencedor(jogador):
        for linha in tabuleiro:
            if all(posicao == jogador for posicao in linha):
                return True
        for coluna in range(3):
            if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
                return True
        if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2-i] == jogador for i in range(3)):
            return True
        return False

    def PosicaoValida():
        while True:
            numero = input()
            try:
                numero = int(numero)
                if numero in range(1, 10):
                    return numero
                else:
                    print("\nNúmero não está no tabuleiro.")
            except ValueError:
                print("\nIsso não é um número. Tente novamente.")
                continue

    def jogadaUsuario(jogador):
        espaco_colocado = PosicaoValida() - 1
        linha = espaco_colocado // 3
        coluna = espaco_colocado % 3
        if tabuleiro[linha][coluna] == "X" or tabuleiro[linha][coluna] == "O":
            print("\nEspaço já ocupado. Tente colocar em outro.")
            jogadaUsuario(jogador)
        else:
            tabuleiro[linha][coluna] = jogador

    def jogadaMaquinaFacil():
        espacos_vazios = [(linha, coluna) for linha in range(3) for coluna in range(3) if tabuleiro[linha][coluna] != "X" and tabuleiro[linha][coluna] != "O"]
        linha, coluna = random.choice(espacos_vazios)
        tabuleiro[linha][coluna] = "O"

    jogadas = 0
    while not vitoria:
        ImprimirTabuleiro()
        vitoria = verificaVencedor("O")
        if vitoria:
            print("Jogador O venceu!")
            imprimePontuacao['Jogador O'] += 1
            break

        if jogadas == 9:
            print("O jogo acabou em empate.")
            imprimePontuacao['Empate'] += 1
            break

        print("Jogador X, escolha um espaço.")
        jogadaUsuario("X")
        jogadas += 1

        ImprimirTabuleiro()
        vitoria = verificaVencedor("X")
        if vitoria:
            print("Jogador X venceu!")
            imprimePontuacao['Jogador X'] += 1
            break

        print("Vez do sistema escolher um espaço.")
        jogadaMaquinaFacil()
        jogadas += 1

ImprimeMenuPrincipal()
