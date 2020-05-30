from forca import Forca
import utils


class ForcaMenu():
    """Executa uma sessão de jogo de forca

    O forcaMenu executa uma sessão de jogo de forca do nome do capeta,
    marcando o histórico das partidas e a pontução do jogador.

    Apresenta um menu de opções e executa cada opção de acordo com a
    escolha feita pelo jogador.
    """

    def __init__(self):
        """Inicia a sessão com dados zerados"""

        self.erase()

    def show_menu(self):
        """
        Exibe o menu de opções da sessão de jogo, com opções pra jogar
        uma partida, ver o placar do jogo, ver o histórico de partidas,
        zerar o placar e encerrar o jogo.
        """

        menu="""---------------------------------------------
Bem vindo ao Jogo da Forca do Nome do Capeta.
---------------------------------------------
Escolha uma opção:

1: Iniciar novo jogo
2: Ver placar
3: Ver histórico
4: Zerar placar
0: Encerrar
---------------------------------------------"""
        print(menu)

    def read_menu_option(self):
        """Lê a opção do jogador, após mostrar o menu.

        Apresenta o menu de opções ao jogador e aguarda a entrada da
        opção esoclhida. A entrada deve ser uma das opções apresentadas
        ao jogador. Qualquer valor que não se encaixe no intervalo será
        rejeitado e o menu será reapresentado.
        """

        keep_ask = True
        choice = 0
        while(keep_ask):
            try:
                self.show_menu()
                choice = int(input("Escolha uma opção: "))
                if(choice < 0 or choice > 4):
                    raise ValueError("ERRO: Valor incorreto. Escolha uma opção entre 0 e 4.")

                keep_ask = False

            except ValueError as err:
                message = "Erro ao informar opção."
                message += f"\nMensagem: {err}"
                utils.print_message_box(message)
                keep_ask = True

        return choice

    def exit(self):
        """Exibe a mensagem de encerramento do jogo."""

        utils.print_message_box("Encerrando o jogo...")

    def show_scoreboard(self):
        """Imprime o placar do jogo."""

        message = f"Vitórias: {self._scoreboard['win']} | Derrotas: {self._scoreboard['lose']}"

        utils.print_message_box(message)

    def show_history(self):
        """Exibe o histórico das partidas

        Exibe o histórico das partidas, com so seguintes dados: qual o
        nome do capeta secreto, quais os erros que o jogador cometeu e
        qual o status da partida(se venceu ou não).
        """

        if(len(self._history) > 0):
            for event in self._history:
                if(event['success']):
                    result = "Vitória"
                else:
                    result = "Derrota"

                message = ""
                message += (f"Nome do capeta: {event['secret']}")
                message += (f"\nErros: {event['misses']}")
                message += (f"\nResultado: {result}")

                utils.print_message_box(message)
        else:
            message = "Nenhum jogo foi registrado até o momento."
            utils.print_message_box(message)

    def erase(self):
        """Inicializa a sessão de jogo

        Inicializa a sessão de jogo, apagando dados do placar e
        limpando o histórico.
        """

        self._scoreboard = {
            'win': 0,
            'lose': 0,
        }

        self._history = []

        utils.print_message_box("Placar zerado com sucesso!")

    def start_game(self):
        """Inicializa uma nova partida

        Inicializa uma nova partida. O resultado da partida é somado ao
        placar o gravado no histórico.
        """

        game = Forca()
        result = game.run()

        if(result['success']):
            self._scoreboard['win'] = self._scoreboard['win'] + 1
        else:
            self._scoreboard['lose'] = self._scoreboard['lose'] + 1

        self._history.append(result)

    def execute(self, choice):
        """Executa uma opção do menu.

        Executa uma das opções que o usuário informou.

        Lança um ValueError se o valor for menor que 0 ou maior que 4.
        """

        if(choice < 0 or choice > 4):
            raise ValueError("O valor informado é invalido. "
                + "Favor escolher um valor entre 0 e 4.")

        options = {
            0: self.exit,
            1: self.start_game,
            2: self.show_scoreboard,
            3: self.show_history,
            4: self.erase,
        }

        func = options.get(choice, "nothing")

        func()

    def run(self):
        """Executa a sessão de jogo até que ela seja encerrada."""
        choice = 1

        while(choice != 0):
            choice = self.read_menu_option()
            self.execute(choice)


if __name__ == "__main__":
    app = ForcaMenu()
    app.run()
