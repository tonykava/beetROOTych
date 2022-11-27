import socket
from threading import Thread

IP = 'localhost'
PORT = 20000
ADDR = (IP, PORT)

def handle_client(connection, addr):
    print(f'[NEW CONNECTION] {addr}')
    connected = True
    while connected:
        data = connection.recv(1024).decode('utf-8')
        if data == 'DISCONNECT!':
            connected = False

        print(f'[{addr}] {data}')
        msg = f'Msg received: {data}'
        connection.send(msg.encode('utf-8'))

    connection.close()



def main():
    print('[STARTING] Server is starting...')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f'[LISTENING] Server is listening on {IP}:{PORT}')

    while True:
        connection, addr = server.accept()
        thread = Thread(target=handle_client, args=(connection, addr,))
        thread.start()
        
if __name__ == '__main__':
    main()