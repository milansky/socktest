import socket

remote_address = "10.11.112.137" # Change this
remote_port = 666
remote_server = (remote_address, remote_port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((socket.gethostname(), remote_port))

s.connect(remote_server)

TEST_CONN = "test conn".encode("utf-8")
#s.send(TEST_CONN)
full_msg = ""
while True:
    msg = s.recv(1024)
    if len(msg) <= 0:
        break
    full_msg += "\n" + msg.decode('utf-8')
print(full_msg)

# s.close()
