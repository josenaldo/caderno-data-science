# 3.7 Crie um algoritmo em Python que peça 2 números, base e expoente,
# calcule e mostre o primeiro número elevado ao segundo número. Não utilize
# a função de potência da linguagem.
from functools import reduce

base = int(input("Informe a base: "))
expoente = int(input("Informe o expoente: "))

multiplicadores = [1]+([base]*expoente)
print(multiplicadores)

potencia = reduce(lambda x, y:x * y, multiplicadores)

print (potencia)