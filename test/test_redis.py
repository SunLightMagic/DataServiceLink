import redis
import time
re = redis.Redis(host='127.0.0.1', port=6379,db=0, password=12345)
#re.set('key_name','value_test')
while True:

    data = re.rpop("recivData")
    print(data)
    time.sleep(0.5)

