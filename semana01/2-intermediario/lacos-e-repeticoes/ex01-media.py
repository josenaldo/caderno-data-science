# Exercicio 1
# Crie um algoritmo que solicite ao usuário 3 números e printe na tela a
# média destes (fácil)

soma = 0
contador = 0

while (contador < 3):
    num = float(input("Informe um número: "))
    soma = soma + num
    contador += 1

media = soma / contador

print(f"a média é {media}")