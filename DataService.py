import sys
import socket
import redis
from configparser import ConfigParser

cfg = ConfigParser()
configfileName = "./config/configration.cfg"
cfg.read(configfileName)
section=cfg.sections()[0]
host = '127.0.0.1'
port = 1885
addr = (host,port)
tcpclient=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpclient.connect(addr)
red = redis.Redis(host='127.0.0.1', port=6379,db=0, password=12345)
while True:
    data = tcpclient.recv(1024)
    #red.lpush("recivData",data)
    print("recieved data from server:",data)