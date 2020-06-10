# 3.6 Crie um algoritmo em Python que leia três números e mostre o maior e
# o menor deles.

lista = []

for i in range(3):
    num = int(input("Informe o número"))
    lista.append(num)

print("Maior:", max(lista))
print("Menor:", min(lista))
