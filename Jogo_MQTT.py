from paho.mqtt import client as mqtt_client


class Game:
    def __init__(self):
        """
        Contrutor do objeto Game
        :var: board
        :return: Jogo da Velha
        """
        self.__broker = '10.21.160.16'
        self.__port = 1883
        self.__topic = "teste"
        self.__client_id = f'diego-9090'
        self.__username = 'diegol'
        self.__password = '12345'
        self.__client = self.connect_mqtt()
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
        linha = 0
        coluna = 0
        while self.vencedor() == 0:
            print(f"\nJogador {jogada%2 + 1}")
            self.tabuleiro()
            if jogada % 2 + 1 == 1:
                linha, coluna = self.publish(self.__client)
            else:
                linha, coluna = self.subscribe(self.__client)
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

    def connect_mqtt(self):
        def on_connect(rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(self.__client_id)
        client.username_pw_set(self.__username, self.__password)
        client.on_connect = on_connect
        client.connect(self.__broker, self.__port)
        return client

    def publish(self, client):
        linha = int(input("\nLinha: "))
        client.publish(self.__topic, linha)
        coluna = int(input("Coluna: "))
        client.publish(self.__topic, coluna)
        return linha, coluna

    def subscribe(self, client: mqtt_client):
        msg_count = 0
        recebidos = []
        while msg_count <= 2:
            def on_message(msg):
                print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
                recebidos.append(msg.payload.decode())
            client.subscribe(self.__topic)
            client.on_message = on_message
            msg_count += 1
        linha = recebidos[0]
        coluna = recebidos[1]
        return linha, coluna


if __name__ == '__main__':
    g1 = Game()
    g1.menu()
