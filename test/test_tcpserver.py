import socket
import time
host='127.0.0.1'
port=1885
addr=(host,port)
tcpSerSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpSerSock.bind(addr)
tcpSerSock.listen(5)
count = 0
while True:
    print('等待客户端连接……')
    tcpCliSock,client_addr=tcpSerSock.accept() #等待接受连接
    print('连接成功，客户端地址为：',client_addr)

    while True:
        '''
        data=tcpCliSock.recv(2048)
        if not data:
            break
        print(data.decode())
        '''

        msg='010000000245'+str(count)
        count += 1
        if not msg:
            print("message error!")
            break;
        tcpCliSock.send(msg.encode())
        print("server send to client data:",msg)

        time.sleep(0.05)
    tcpClisock.close()
tcpSerSock.close()
