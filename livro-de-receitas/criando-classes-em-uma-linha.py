# Para criar uma classe simples, cuja função é apenas armazenr atributos,
# você pode usar uma namedtuple
import collections

Carta = collections.namedtuple('Carta', ['valor', 'naipe'] )

zape = Carta(4, "paus")

print(zape)