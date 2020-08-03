# 3.12 Crie uma classe que modele uma pessoa:

# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer.

# Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.


class Pessoa(object):
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade = self.idade + 1

        if(self.idade < 21):
            self.altura = self.altura + 0.5

    def engordar(self, peso_a_mais):
        self.peso = self.peso + peso_a_mais

    def emagrecer(self, peso_a_menos):
        self.peso = self.peso - peso_a_menos

    def crescer(self, altura_a_mais):
        self.altura = self.altura + altura_a_mais

    def __repr__(self):
        return (
            f"Pessoa("
            f"Nome: {self.nome} "
            f"| Idade: {self.idade} "
            f"| Peso: {self.peso} "
            f"| Altura: {self.altura} "
            f")"
        )


if __name__ == "__main__":
    josenaldo = Pessoa("Josenaldo", 39, 88, 1.86)

    print(josenaldo)