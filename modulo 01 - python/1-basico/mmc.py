a = int(input("Insira o primeiro número: "))
b = int(input("Insira o segundo número: "))

x = a
y = b
resto = None

while (resto != 0):
    resto = x % y
    x = y
    y = resto

mdc = x

mmc = (a * b) / mdc

print(f"O MMC de {a} e {b} é {mmc}")