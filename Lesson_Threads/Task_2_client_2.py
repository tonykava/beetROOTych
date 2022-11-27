import socket

IP = 'localhost'
PORT = 20000
ADDR = (IP, PORT)

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f'[CONNECTED] Client connected to server at {IP}:{PORT}')
    connected = True

    while connected:
        msg = input('Enter your msg > ')

        client.send(msg.encode('utf-8'))

        if msg == 'DISCONNECT!':
            connected = False
        else:
            msg = client.recv(1024).decode('utf-8')
            print(f'[SERVER] {msg}')

if __name__ == "__main__":
    main()