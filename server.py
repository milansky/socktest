import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.11.112.137', 666))

while True:

    sock.listen(5)
    clientsocket, address = sock.accept()
    print(f'New connection from {address} has been established')
    clientsocket.send(b'Welcome to the server')
    clientsocket.close()
