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
redisPool = redis.ConnectionPool(host='localhost', port=6379,db=8, password=12345)
redClient = redis.Redis(connection_pool=redisPool)
while True:
    data = tcpclient.recv(1024)
    redClient.lpush("parkmsg",data.decode())
    print("recieved data from server:",data.decode())