import forca
import adivinhacao


def escolhe_jogo():
    print("*********************************")
    print("*******Bem vindo ao jogos!*******")
    print("*********************************")

    print("Escolha qual jogo deseja jogar: \n(1) Adivinhacao \n(2) Forca")
    print("*********************************")
    jogo = int(input("Digite o número do jogo desejado: "))

    if (jogo == 1):
        print("Iniciando adivinhação")
        adivinhacao.jogar()
    elif (jogo == 2):
        print("Iniciando forca")
        forca.jogar()


if (__name__ == "__main__"):  # executando diretamente
    escolhe_jogo()
