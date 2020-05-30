import random

from forca_palavras import DEVIL_NAMES
from forca_enforcado import HANGED
import utils


class Forca:
    """Representa uma partida de forca

    Classe qeu representa uma partida do jogo de forca. O jogo começa
    com a escolha aleatória de um nome do capeta. O jogo então mostra,
    ao jogador, um underscores para cada letra do nome do capeta.
    O jogador então informa uma letra por rodada. Se acertar a letra,
    ela é revelada na posição (ou nas posições) em que se encontra na
    palavra. Se o jogador acertar a palavra, ele vence. Se errar 7
    vezes, o enforcado aparece e ele perde.
    """

    def __init__(self):
        """Inicializa o jogo de forca

        Inicializa o jogo de forca, zerando os erros, o indicador de
        sucesso e de enforcamento, a nome do capeta secreto e a lista
        de erros do jogador.
        """
        self._success = False
        self._hanged = False
        self._secret = None
        self._guess = None
        self._word_dashes = None
        self._errors = 0
        self._misses = []

    def show_welcome(self):
        """Exibe a mensagem de boas vindas

        Exibe uma mensagem de boas vindas sobre o jogo
        """
        message = "*** Iniciando a partida do Jogo da Forca do Nome do Capeta ***"
        utils.print_message_box(message)

    def select_secret_devil_name(self):
        """Escolhe um nome do capeta para o jogo

        Escolhe, aleatoriamente, um nome do capeta para o jogo. Depois,
        inicia a lista de tentativas e os a lista de traços. Os espaços
        entre as palavras são revelados na lista de traços.
        """
        self._secret = random.choice(DEVIL_NAMES).upper()
        self._word_dashes = ["_"] * len(self._secret)
        self.put_guess_in_word_dashes(" ")

    def read_player_move(self):
        """Lê o movimento do jogador

        Mostra, ao jogador, o enforcado e como está o status do jogo.
        Depois, pede por uma tentativa. O usuário deve informar uma
        letra apenas.
        """
        self.show_hanged()
        print("Nome do Capeta:", " ".join(self._word_dashes))
        print("Tentativas:", "-".join(self._misses))

        try_again = True
        guess = None

        while(try_again):
            guess = input("Informe uma nova letra: ")

            if(len(guess) == 1 and guess.isalpha()):
                self._guess = guess.upper()
                try_again = False
            else:
                print("Valor incorreto. Informe uma letra.")

        return guess

    def put_guess_in_word_dashes(self, player_guess):
        """ Coloca o caracter informado pelo jogador na lista de traços

        Varre o nome do capeta e, pra cada caracter, testa se é igual
        à tentativa. Se for, coloca esse caracter na posição
        equivalente na lista de traços.
        """

        for i in range(len(self._secret)):
            letter = self._secret[i]
            if(letter == player_guess.upper()):
                self._word_dashes[i] = letter

    def verify_continue(self):
        """Verifica se o jogo continua

        Verifica se o jogador ganhou ou se o jogador foi enforcado.
        Esses valores são usados pra determinar se mais uma rodada irá
        ocorrer
        """
        name = "".join(self._word_dashes)

        self._success = self._secret == name
        self._hanged = self._errors == 6

    def game_must_continue(self):
        """Indica se o jogo deve ou não continuar

        Indica se o jogo deve ou não continuar a partir do status de
        vitória e do status de enforcado. O jogo pára quando o jogador
        for enforcado ou quando o jogador acertar o nome do capeta
        secreto.
        """
        return not self._success and not self._hanged

    def show_hanged(self):
        """Imprime o enforcado

        Imprime o enforcado, de acordo com o número de erros.
        """
        print(HANGED[self._errors])

    def show_score(self):
        """Imprime o score da partida

        Imprime o score final da partida, indicando o status de vitória
        e o nome do capeta secreto.
        """
        if(self._success):
            message = f"Parabéns, você acertou o nome do capeta!"
            message +=f"\n---{self._secret}---"
            utils.print_message_box(message)
        else:
            message = f"Sinto muito mas você errou o nome do capeta "
            message +=f"e foi enforcado!"
            message +=f"\n---{self._secret}---"
            utils.print_message_box(message)

            self.show_hanged()

    def run(self):
        """Executa o jogo

        Método que executa o jogo continuamente, até que o jogador
        escolha a palavra certa ou falhe.
        """

        # mensage inicial
        self.show_welcome()

        # Ler a palavra secreta
        self.select_secret_devil_name()

        # enquanto não enforcou e não acertou
        while(self.game_must_continue()):

            # leia um caracter do jogador
            player_move = self.read_player_move()

            # compara caracter com palavra secreta
            # se acertou caracter
            if(player_move.upper() in self._secret):
                # exibe caracter em espaços
                self.put_guess_in_word_dashes(player_move)
            else:
                # incrementa contador de erros
                self._errors += 1
                self._misses.append(player_move)

            # verifica se continua
            self.verify_continue()

        # mostra a pontuação
        self.show_score()

        history = {
            'success': self._success,
            'secret': self._secret,
            'misses': " ".join(self._misses),
        }
        return history


if __name__ == "__main__":
    jogo = Forca()
    jogo.run()