from functools import reduce


# Exercício 2
# Crie um algoritmo que solicite ao usuário um número e apresente o fatorial
# deste número como resultado (médio) Clique aqui para saber como calcular o
# fatorial.

n = int(input("Informe um número positivo: "))

fatorial = reduce((lambda x,y:x*y), range(1, n + 1))

print(f"{n}! = {fatorial}")