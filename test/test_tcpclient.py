import sys
import socket

host = '127.0.0.1'
port = 1885
addr = (host,port)
tcpclient=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpclient.connect(addr)
while True:
    data = tcpclient.recv(1024)
    print("client recive data from server:",data)