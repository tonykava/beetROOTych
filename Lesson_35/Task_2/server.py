import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 20000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

def ceaser(data, key=1):
    result = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    ualpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in data:
        if i in alpha:
            result += alpha[(alpha.index(i) + int(key)) % 26]
        elif i in ualpha:
            result += ualpha[(ualpha.index(i) + int(key)) % 26]
        else:
            result += i
    return result


while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                data = data.decode('utf-8')
                connection.sendall(bytes(ceaser(data.split('///')[0], int(data.split('///')[-1])), 'utf-8'))
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
