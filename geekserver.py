import socket

s = socket.socket()

port = 9812

s.bind(('', port))
print('[*] bind socket to port: %s.' %(port))

s.listen(5)
print('[*] port started listening.')

while True:
    c, addr = s.accept()
    print('[*] connection recieved addr: ' + str(addr) + '.')

    c.send(b'this is some response')
    print('[*] response sended back.')

    c.close()
