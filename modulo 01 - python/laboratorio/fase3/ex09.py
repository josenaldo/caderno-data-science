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

from functools import reduce
from collections import namedtuple

ano_atual = 1997
# ano_atual = int(input("Informe o ano atual: "))

ano_inicio = 1995
tempo =  ano_atual - ano_inicio
print(f"tempo: {tempo}")

salario_inicial = 1000
aumento_base = 0.015
fator_de_aumento = 2

calcula_aumento  = lambda ano: (salario_inicial if ano == 0 else calcula_aumento(ano -1) + (calcula_aumento(ano -1) * (aumento_base * (2 ** (ano-1)))))

print(f"O salário, no ano de {ano_atual} foi de R$ {calcula_aumento(tempo):.2f}")

