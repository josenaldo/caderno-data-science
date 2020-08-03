# Exercício 3
# Crie um algoritmo que solicite 5 números. Ao término, printar o maior e o
# menor número (difícil)

numeros = []

for x in range(1, 6):
    num = int(input("Informe um número: "))
    numeros.append(num)

maior = max(numeros)
menor = min(numeros)

print(f"Maior: {maior} | Menor: {menor}")
