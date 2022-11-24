import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 20000        # The port used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        msg = bytes(input('Give ur input in format: string///key  where key is integer: '), 'utf-8')
        s.sendall(msg)
        data = s.recv(1024).decode('utf-8')

print('Received: ', data)

