from time import sleep
import random
from historia import historia_Mostrar

historia_Mostrar()

#variável de controle da repetição
repetir = "sim"

numero_Random1 = random.randint(1,9)
numero_Random2 = random.randint(1,9)
numero_Random3 = random.randint(1,9)

senhacompleta = str(numero_Random1) + str(numero_Random2) + str(numero_Random3)

print(senhacompleta)

while repetir == "sim":
    # mostra o menu
    print("Selecione um objeto:")
    print("0 - Porta")
    print("1 - Janela")
    print("2 - Mochila")
    print("3 - Vaso")
    print("4 - Gaveta")
    print("5 - Quadro")
    print("6 - Baú")
    print("7 - Tapete")
    print("8 - Espelho")
    print("9 - Estante")
    # pega a opção escolhida
    resposta = input("Digite um número de 0 a 9: ")

    # se escolheu a porta:
    if(resposta == "0"):
        print("Você vai até a porta. Na fechadura, você deve colocar uma senha de 3 dígitos.")
        print(senhacompleta)
        # pede pra digitar a senha
        senhaJogador = input("Informe a senha: ")
        # se a senha estiver correta, abre a porta
        if(senhaJogador == senhacompleta):
            print("O cadeado abriu!")
            break
        
        else:
            print("errou a senha!")
        # se errar a senha, volta para o menu 

print("Parabéns! Você terminou o jogo.")
