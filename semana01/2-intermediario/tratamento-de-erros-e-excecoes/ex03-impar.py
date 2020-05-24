# Crie um código em Python que peça um número ímpar do usuário. Caso o número
# seja par, apresente mensagem guiando o usuário até o preenchimento correto
# (Difícil)

continua = True

while(continua):
    try:
        numero = int(input("Digita um número: "))

        if (numero % 2 == 0):
            raise ValueError(f"O valor informado ({numero}) é par. Deve ser informado um número ímpar.")

        print(f"Parabéns! O número ({numero}) informado é impar!")
        continua = False

    except ValueError as error:
        continua = True
        print(error)
