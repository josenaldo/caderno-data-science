# 3.8 Crie um algoritmo em Python que peça 10 números inteiros, calcule
# e mostre a quantidade de números pares e a quantidade de números impares.

lista = []
for i in range(10):
    num = int(input("Informe um número: "))
    lista.append(num)

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 8]

total = len(lista)
impares = len(list(filter(lambda x: x % 2, lista)))
pares = total - impares

print(F"Impares: {impares}")
print(F"Pares: {pares}")
