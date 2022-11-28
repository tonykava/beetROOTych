import asyncio, socket

async def handle_client(connection, addr):
    print(f'[NEW CONNECTION] {addr}')
    loop = asyncio.get_event_loop()
    connected = True
    while connected:
        data = (await loop.sock_recv(connection, 1024)).decode('utf-8')
        if data == 'DISCONNECT!':
            connected = False

        print(f'[{addr}] {data}')
        msg = f'Msg received: {data}'
        await loop.sock_sendall(connection, msg.encode('utf-8'))

    connection.close()


async def run_server():
    IP = 'localhost'
    PORT = 15555
    ADDR = (IP, PORT)
    print('[STARTING] Server is starting...')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ADDR))
    server.listen(8)
    print(f'[LISTENING] Server is listening on {IP}:{PORT}')


    loop = asyncio.get_event_loop()

    while True:
        connection, addr = await loop.sock_accept(server)
        loop.create_task(handle_client(connection, addr))

asyncio.run(run_server())