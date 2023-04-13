import threading
import socket

clients = []


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

    def jogo(self):
        """
        Confere de quem é a vez de jogar e pede para que o jogador insira um valor para a linha e um para a coluna.
        Após isso, ele testa, chamando a função vencedor(), se um, dos jogadores venceu o jogo.
        """
        self.jogada = 0
        while self.vencedor() == 0:
            if self.jogada % 2 + 1 == 1:
                self.tabuleiro(clients[0])
                self.sendMessages(self.server)
            elif self.jogada % 2 + 1 == 2:
                self.tabuleiro(clients[1])
                self.sendMessages(self.server)

            if self.pos == 0:
                linha = 1
                coluna = 1
            elif self.pos == 1:
                linha = 1
                coluna = 2
            elif self.pos == 2:
                linha = 1
                coluna = 3
            elif self.pos == 3:
                linha = 2
                coluna = 1
            elif self.pos == 4:
                linha = 2
                coluna = 2
            elif self.pos == 5:
                linha = 2
                coluna = 3
            elif self.pos == 6:
                linha = 3
                coluna = 1
            elif self.pos == 7:
                linha = 3
                coluna = 2
            elif self.pos == 8:
                linha = 3
                coluna = 3

            if self.__board[linha-1][coluna-1] == 0:
                if (self.jogada % 2 + 1) == 1:
                    self.__board[linha - 1][coluna - 1] = 1
                else:
                    self.__board[linha - 1][coluna - 1] = -1
            else:
                print("Não esta vazio")
                self.jogada -= 1
                matriz_ = self.matriz
                print(matriz_)

            if self.vencedor():
                print("-" * 20)
                print(f"Jogador {self.jogada%2 + 1} ganhou após {self.jogada+1} rodadas")
                print("-" * 20)
                self.tabuleiro(clients[self.jogada%2])
                print("-" * 20)
            self.jogada += 1

    def vencedor(self):
        """
        Testa se um dos jogadores foi vencedor, retornando para a função jogo o resultado do teste.
        :return: Boolean
        """
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

    def tabuleiro(self, client):
        """
        Tem a função de mostrar o tabuleiro para os usuários, imprimindo a matriz.
        """
        for i in range(3):
            for j in range(3):
                if self.__board[i][j] == 0:
                    print(" _ ", end=' ')
                elif self.__board[i][j] == 1:
                    print(" X ", end=' ')
                elif self.__board[i][j] == -1:
                    print(" O ", end=' ')

            print()

    @property
    def matriz(self):
        return self.__board



    def main(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.server.bind(('localhost', 5050))
            self.server.listen()
        except:
            return print('\nNão foi possível iniciar o servidor!\n')

        while True:
            client, addr = self.server.accept()
            clients.append(client)

            thread = threading.Thread(target=self.messagesTreatment, args=[client])
            thread.start()
            thread2 = threading.Thread(target=self.jogo(), args=[client])
            thread2.start()
            self.jogo()

    def messagesTreatment(self, client):
        while True:
            try:
                msg = client.recv(2048)
                self.broadcast(msg, client)
                pos_str = msg
                self.pos = int(pos_str)
            except:
                self.deleteClient(client)
                break

    def broadcast(self, msg, client):
        for clientItem in clients:
            if clientItem != client:
                try:
                    clientItem.send(msg)
                except:
                    self.deleteClient(clientItem)

    def deleteClient(self, client):
        clients.remove(client)

    def sendMessages(self, server):
        while True:
            try:
                msg = input(self.matriz)
                server.send(f'Vez do Jogador:{self.jogada%2+1}\n{msg}'.encode('utf-8'))
            except:
                return


if __name__ == '__main__':
    g1 = Game()
    g1.main()
