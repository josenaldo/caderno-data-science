# 3.4 Supondo que a população de um país A seja da ordem de 80000
# habitantes com uma taxa anual de crescimento de 3% e que a população
# de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Crie um algoritmo em Python que calcule e escreva o número de anos
# necessários para que a população do país A ultrapasse ou iguale a
# população do país B, mantidas as taxas de crescimento.

def calcula_populacao_total(populacao_inicial, taxa):

    aumento_populacional = populacao_inicial * taxa
    populacao_total = populacao_inicial + aumento_populacional

    return populacao_total

populacao_inicial_a = 80000
taxa_a = 0.03

populacao_inicial_b = 200000
taxa_b = 0.015

i = 0
total_a = populacao_inicial_a
total_b = populacao_inicial_b

while (total_a <= total_b):
    i = i + 1
    total_a = calcula_populacao_total(total_a, taxa_a)
    total_b = calcula_populacao_total(total_b, taxa_b)

print (f"Serão precisos {i} anos pra população de A superar a população de B")
