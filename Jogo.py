class Game:
    def __init__(self):
        """
        Contrutor do objeto Game
        :var: board matriz de ints
        :return: Jogo da Velha
        """
        self.__board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        print("-" * 20)
        print("JOGO DA VELHA")
        self.jog1 = 1
        self.jog2 = -1

    def menu(self):
        """
        Mostra um menus para o usuário, onde ele tem a opção de Jogar ou de Encerrar o programa.
        :var: continuar int
        """
        continuar = 1
        while continuar:
            print("-" * 20)
            continuar = int(input("0 - Sair\n1 - Jogar\n"))
            print("-" * 20)
            if continuar:
                self.jogo()
            else:
                print("Jogo Finalizado")

    def jogo(self):
        """
        Confere de quem é a vez de jogar e pede para que o jogador insira um valor para a linha e um para a coluna.
        Após isso, ele testa, chamando a função vencedor(), se um, dos jogadores venceu o jogo.
        :var: jogada int
        :var: linha int
        :var: coluna int
        """
        jogada = 0
        while self.vencedor() == 0:
            print(f"\nJogador {jogada % 2 + 1}")
            self.tabuleiro()
            linha = int(input("\nLinha: "))
            coluna = int(input("Coluna: "))

            try:
                if self.__board[linha - 1][coluna - 1] == 0:
                    if (jogada % 2 + 1) == 1:
                        self.__board[linha - 1][coluna - 1] = 1
                    else:
                        self.__board[linha - 1][coluna - 1] = -1
                else:
                    print("Não esta vazio")
                    jogada -= 1
                    matriz_ = self.matriz
                    print(matriz_)

                if self.vencedor():
                    print("-" * 20)
                    print(f"Jogador {jogada % 2 + 1} ganhou após {jogada + 1} rodadas")
                    print("-" * 20)
                    self.tabuleiro()
                    print("-" * 20)
                jogada += 1
            except:
                self.set_board = 0

    def vencedor(self):
        """
        Testa se um dos jogadores foi vencedor, retornando para a função jogo o resultado do teste.
        :return: Boolean
        """
        for i in range(len(self.__board) - 1):
            if self.__board[i][0] + self.__board[i][1] + self.__board[i][2] == 3 or self.__board[i][0] + \
                    self.__board[i][1] + self.__board[i][2] == -3:
                return True
        for i in range(len(self.__board) - 1):
            if self.__board[0][i] + self.__board[1][i] + self.__board[2][i] == 3 or self.__board[0][i] + \
                    self.__board[1][i] + self.__board[2][i] == -3:
                return True
        if self.__board[0][0] + self.__board[1][1] + self.__board[2][2] == 3 or self.__board[0][0] + self.__board[1][
            1] + self.__board[2][2] == -3:
            return True
        if self.__board[0][2] + self.__board[1][1] + self.__board[2][0] == 3 or self.__board[0][2] + self.__board[1][
            1] + self.__board[2][0] == -3:
            return True
        return False

    def tabuleiro(self):
        """
        Tem a função de mostrar o tabuleiro para os usuários, imprimindo a matriz.
        """

        for i in range(3):
            for j in range(3):
                if self.__board[i][j] == 0:
                    print(" _ ", end=' ')
                elif self.__board[i][j] == self.jog1:
                    print(" X ", end=' ')
                elif self.__board[i][j] == self.jog2:
                    print(" O ", end=' ')

            print()

    @property
    def matriz(self):
        return self.__board

    @property
    def set_board(self):
        return self.__board

    @set_board.setter
    def set_board(self, new):
        self.__board = [[new, new, new], [new, new, new], [new, new, new]]


if __name__ == '__main__':
    g1 = Game()
    g1.menu()
