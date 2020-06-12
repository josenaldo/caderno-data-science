from random import shuffle

# Para embaralhar uma lista, use a função random.shuffle
lista = list(range(20))
print("Lista normal".center(30,"*", ))
print(lista)

shuffle(lista)
print("Lista embaralhada".center(30,"*", ))
print(lista)
