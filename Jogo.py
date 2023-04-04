class Game:
    def __init__(self):
        """
        Contrutor do objeto Game
        :var: board
        :return: Jogo da Velha
        """
        self.__board = [[0,0,0],[0,0,0],[0,0,0]]
        print("OBJETO INSTANCIADO", self)

    def menu(self):
        continuar = 1
        while continuar:
            continuar = int(input("0 - Sair\n1 - Jogar Novamente"))
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
                print(f"Jogador {jogada%2 + 1} ganhou após {jogada+1} rodadas")
                self.tabuleiro()

    def vencedor(self):

    def tabuleiro(self):

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
