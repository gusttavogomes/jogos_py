import random


def jogar():

    numero = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")
    print("***Qual o nível de dificuldade?*** \n (1) Fácil | (2) Médio | (3) Difícil")
    nivel = int(input("Qual o nível: "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    # while (rodada <= total_tentativas):
    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        print(numero)  # print de teste com o numero a ser acertado
        chute_str = input('Digite o numero: ')
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100:')
            continue

        acertou = numero == chute
        maior = chute > numero

        if (acertou):
            print('Acertou!')
            break
        else:
            if (maior):
                print("Errou. Chute foi maior")
            else:
                print("Errou. Chute foi menor")
            pontos_perdidos = abs(numero - chute)
            pontos = pontos - pontos_perdidos

    print("\n --- Fim de jogo ---\n Pontuação: {}".format(pontos))


if (__name__ == "__main__"):  # executando diretamente
    jogar()
