import threading
import socket


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 5050))
    except:
        return print('\nNão foi possívvel se conectar ao servidor!\n')

    username = input('Usuário> ')
    print('\nConectado')

    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client, username])

    thread1.start()
    thread2.start()


def receiveMessages(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(msg + '\n')
        except:
            print('\nNão foi possível permanecer conectado no servidor!\n')
            print('Pressione <Enter> Para continuar...')
            client.close()
            break


def sendMessages(client, username):
    while True:
        try:
            msg = input('\n')
            client.send(f'<{username}> {msg}'.encode('utf-8'))
        except:
            return



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


main()
