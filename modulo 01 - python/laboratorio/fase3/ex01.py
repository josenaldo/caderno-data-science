while True:
    try:

        numero = int(input("Insira um número entre 0 e 100: "))

        if(numero < 0):
            raise ValueError(f"Valor '{numero}' é menor que 0, portanto é inválido.")
        elif(numero > 100):
            raise ValueError(f"Valor '{numero}' é maior que 100, portanto é inválido.")
        else:
            print(f"Número informado: {numero}")
            break;
    except ValueError as error:
        print("Ocorreu um erro durante a execução do sistema.")
        print(f"\tMensagem: {error}")