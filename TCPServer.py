import socket

port = 15270
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    soc.bind(('', port))
except socket.error as exception:
    print('Error!:' + `exception`)

soc.listen(1)
conn, addr = soc.accept()
while 1:
    msg = conn.recv(128)
    if not msg: break
    conn.send(msg.encode())
conn.close()
