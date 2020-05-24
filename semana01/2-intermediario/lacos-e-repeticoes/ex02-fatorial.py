# Exercício 2
# Crie um algoritmo que solicite ao usuário um número e apresente o fatorial
# deste número como resultado (médio) Clique aqui para saber como calcular o
# fatorial.

n = int(input("Informe um número positivo"))

num = n
fatorial = 1

while(num > 0):
    fatorial = fatorial * num
    num = num -1

print(f"{n}! = {fatorial}")