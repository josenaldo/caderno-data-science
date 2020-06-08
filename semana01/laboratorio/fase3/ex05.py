# 3.5 Desenvolva um gerador de tabuada, capaz de gerar a tabuada de
# qualquer número inteiro entre 1 a 10. O usuário deve informar de
# qual numero ele deseja ver a tabuada. A saída deve ser conforme o
# exemplo abaixo: Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

numero = int(input("Informe um número: "))

tabuadas = list(map(lambda x: f"{numero} x {x + 1} = {numero * (x + 1)}",range(10)))

for t in tabuadas:
    print(t)