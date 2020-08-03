# 3.2 Crie um algoritmo em Python que leia um nome de usuário e a sua senha e
# não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro
# e voltando a pedir as informações.


while(True):
    try:  
        login = input("Informe seu login: ")
        senha = input("Informe sua senha: ")

        if(login == senha):
            raise ValueError("A senha não pode ser igual ao login")
        else:
            print(f"Bem vindo ao sistema, {login}")
            break
    except ValueError as error:
        print("Ocorreu um erro durante a execução do sistema.")
        print(f"\tMensagem: {error}")