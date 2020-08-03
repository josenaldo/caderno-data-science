# 3.10 Crie um algoritmo em Python com uma função que necessite de um
# argumento. A função retorna o valor de caractere ‘P’, se seu argumento
# for zero ou positivo, e ‘N’, se seu argumento for negativo.

numero = int(input("Informe um número: "))
print((lambda x: 'P' if x >= 0 else 'N')(numero))