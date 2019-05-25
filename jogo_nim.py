def usuario_escolhe_jogada(n, m):
    while True:
        num = int(input('Quantas peças você vai tirar? '))
        if num > m or (n - num) < 0:
            print('Oops! Jogada inválida! Tente de novo.')
        else:
            if num < 2:
                print('Você tirou uma peça.')
            else:
                print('Você tirou', num, 'peças.')
            return num

def multiplo(n, m):
    mult = False
    if n % (m + 1) == 0:
        mult = True
    return mult
        
def computador_escolhe_jogada(n, m):
    qt = 0
    if n <= m:
        qt = n
    else:
        if multiplo(n, m):
            qt = m
        else:
            pc = 0
            while pc % (m + 1) != n % (m + 1):
                pc = pc + 1
                if pc % (m + 1) == n % (m + 1):
                    qt = pc
                    break

    if qt < 2:
        print('O computador tirou uma peça.')
    else:
        print('O computador tirou', qt, 'peças.')
    return qt

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    if multiplo(n, m):
        print('Você começa!')
        jogador = 1
    else:
        print('Computador começa')
        jogador = 0

    while n > 0:
        if jogador == 0:
            n = n - computador_escolhe_jogada(n, m)
            jogador = 1
        else:
            n = n - usuario_escolhe_jogada(n, m)
            jogador = 0
        if n == 0 and jogador == 0:
            print('Fim do jogo! Você ganhou!')
            break
        elif n == 0 and jogador == 1:
            print('Fim do jogo! O computador ganhou!')
            break
        
        if n < 2:
            print('Agora resta apenas uma peça no tabuleiro.')
        else:
            print('Agora restam', n, 'peças no tabuleiro.')

def campeonato():
    print('Você escolheu um campeonato!')
    rodada = 1

    while rodada <= 3:
        print('**** Rodada:', rodada, ' ****')
        partida()
        rodada = rodada + 1
    print('**** Final do campeonato ****')
    print('Placar: Você 0 X', (rodada - 1), 'Computador')

print('Bem-vindo ao jogo do NIM! Escolha:')
option = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato '))

if option == 1:
    print('Você escolheu uma parrtida isolada!')
    partida()
elif option == 2:
    campeonato()