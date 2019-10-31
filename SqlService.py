import pymysql
import redis
import threading
import time
class SqlConsumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.host='localhost'
        self.port=6379
        self.db=8
        self.passwd=12345
        self.msglist = 'parkmsg'
    def run(self):
        while True:
            re = redis.StrictRedis(host=self.host, port=self.port, db=self.db, password=self.passwd)
            data = re.rpop(self.msglist)
            if data is not None:
                print(data.decode())
            time.sleep(0.1)

if __name__ == '__main__':
    a=0
    while a<21:
        thread = SqlConsumer()
        thread.start()
        thread.join(1)
