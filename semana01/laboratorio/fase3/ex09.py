# 3.9 Um funcionário de uma empresa recebe aumento salarial anualmente.
# Sabe-se que:
# - Esse funcionário foi contratado em 1995, com salário inicial de
#   R$ 1.000,00;
# - Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# - A partir de 1997 (inclusive), os aumentos salariais sempre correspondem
# ao dobro do percentual do ano anterior.
#
# Crie um algoritmo em Python que determine o salário atual desse funcionário.
# Após concluir isto, altere o programa permitindo que o usuário digite
# o salário inicial do funcionário.

ano_inicio = 1995
ano_atual = 2020
anos = ano_inicio - ano_atual
anos = list(range(anos))
print(anos)



salario_inicial = 1000

aumento_inicial = 1.5
fator = 2



salario_total  = salario_anterior + (salario_anterior * (percentual_de_aumento * 2 ** ano))
