class Game:
    def __init__(self):
        """
        Contrutor do objeto Game
        :var: board
        :return: Jogo da Velha
        """
        self.__board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        print("-" * 20)
        print("JOGO DA VELHA")

    def menu(self):
        continuar = 1
        while continuar:
            print("-"*20)
            continuar = int(input("0 - Sair\n1 - Jogar\n"))
            print("-" * 20)
            if continuar:
                self.jogo()
            else:
                print("Jogo Finalizado")

    def jogo(self):
        jogada = 0
        while self.vencedor() == 0:
            print(f"\nJogador {jogada%2 + 1}")
            self.tabuleiro()
            linha = int(input("\nLinha: "))
            coluna = int(input("Coluna: "))

            if self.__board[linha-1][coluna-1] == 0:
                if (jogada % 2 + 1) == 1:
                    self.__board[linha - 1][coluna - 1] = 1
                else:
                    self.__board[linha - 1][coluna - 1] = -1
            else:
                print("Não esta vazio")
                jogada -= 1

            if self.vencedor():
                print("-" * 20)
                print(f"Jogador {jogada%2 + 1} ganhou após {jogada+1} rodadas")
                print("-" * 20)
                self.tabuleiro()
                print("-" * 20)
            jogada += 1

    def vencedor(self):
        for i in range(len(self.__board)-1):
            if self.__board[i][0] + self.__board[i][1] + self.__board[i][2] == 3 or self.__board[i][0] + self.__board[i][1] + self.__board[i][2] == -3:
                return True
        for i in range(len(self.__board)-1):
            if self.__board[0][i] + self.__board[1][i] + self.__board[2][i] == 3 or self.__board[0][i] + self.__board[1][i] + self.__board[2][i] == -3:
                return True
        if self.__board[0][0] + self.__board[1][1] + self.__board[2][2] == 3 or self.__board[0][0] + self.__board[1][1] + self.__board[2][2] == -3:
            return True
        if self.__board[0][2] + self.__board[1][1] + self.__board[2][0] == 3 or self.__board[0][2] + self.__board[1][1] + self.__board[2][0] == -3:
            return True
        return False

    def tabuleiro(self):
        for i in range(3):
            for j in range(3):
                if self.__board[i][j] == 0:
                    print(" _ ", end=' ')
                elif self.__board[i][j] == 1:
                    print(" X ", end=' ')
                elif self.__board[i][j] == -1:
                    print(" O ", end=' ')

            print()

"""
    def extrato(self):
        print("TITULAR:", self.__titular, "SALDO:", self.__saldo)

    def __pode_sacar(self, valor_saque: float):  # Abstração
        if valor_saque > self.__saldo:
            return False
        return True

    def sacar(self, valor: float):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print(f"VALOR SACADO: {valor} | NOVO EXTRATO: {self.__saldo}")
        else:
            print("O VALOR PASSOU DOS LIMITES")

    def depositar(self, valor: float):
        self.__saldo += valor

    def tranferir(self, valor: float, destino):
        self.sacar(valor)
        destino.depositar(valor)
        print(f"TRANSFERÊNCIA NO VALOR DE R${valor} DE '{self.__titular}' PARA '{destino.__titular}'")

    @property
    def limite(self):  # Abstração
        return self.__limite

    @limite.setter
    def limite(self, valor):
        if valor > 1.1 * self.__limite:
            print("INFELIZMENTE O LIMITE ESTÁ ACIMA DE 10%")
            print("LIMITE NÃO ALTERADO:", self.limite)
        else:
            self.__limite = valor
            print("LIMITE ALTERADO COM SUCESSO")
            print("NOVO VALOR:", self.limite)


class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property  # Getter -> ele é acessado por uma funçãe e não um atributo.
    def nome(self):
        print("CHAMANDO GETTER NOME")
        return self.__nome.title()

    @nome.setter  # Setter -> altera um atributo do meu objeto.
    def nome(self, nome):
        print("CHAMANDO SETTER NOME")
        self.__nome = nome
"""

if __name__ == '__main__':
    g1 = Game()
    g1.menu()
