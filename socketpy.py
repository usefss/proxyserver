
import sys
import socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ('[*] socket created.')
except socket.error as e:
    print('[*] err: socket failed to create with message: ')
    print (e.message)

port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
    print('[*] host ip captured: %s'%(host_ip))
except socket.gaierror as e:
    print('[*] err: host ip do not resolved with message: ')
    print(e.message)
    sys.exit()

try:
    print('[*] connecting to server ...')
    s.connect((host_ip, port))
    print('[*] socket connected to host on:' + str(host_ip) + ':' + str(port))
except:
    print('[*] err: failed to connect.')
