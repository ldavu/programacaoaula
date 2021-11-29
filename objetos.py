def investigar_porta(parsenhacompleta):
    
    print("Você vai até a porta. Na fechadura, você deve colocar uma senha de 3 dígitos.")
    print(parsenhacompleta)
        
    # pede pra digitar a senha

    senhaJogador = input("Informe a senha: ")

    # se a senha estiver correta, abre a porta
    if(senhaJogador == parsenhacompleta):
        print("O cadeado abriu!")
        return False
    else:
        print("errou a senha!")
        # se errar a senha, volta para o menu 
        return True
        
