import socket

s = socket.socket()

port = 98012

s.bin(('', port))
print('[*] bind socket to port: %s.' %(port))

s.listen(5)
print('[*] port started listening.')

while True:
    c, addr = s.accept()
    print('[*] connection recieved addr: %s.' %addr)

    c.send('this is some response')
    print('[*] response sended back.')

    c.close()
    
