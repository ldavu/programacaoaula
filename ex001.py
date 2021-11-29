from time import sleep
import random
from historia import historia_Mostrar
from menu import mostrarMenu
import objetos

# historia_Mostrar()

#variável de controle da repetição
repetir = True

numero_Random1 = random.randint(1,9)
numero_Random2 = random.randint(1,9)
numero_Random3 = random.randint(1,9)

senhacompleta = str(numero_Random1) + str(numero_Random2) + str(numero_Random3)

print(senhacompleta)

while repetir == True:
    
    opcao = mostrarMenu()


    # se escolheu a porta:

    if(opcao == "0"):

        repetir = objetos.investigar_porta(senhacompleta)


print("Parabéns! Você terminou o jogo.")
