import redis
import time
re = redis.Redis(host='localhost', port=6379,db=8, password=12345)
#re.set('key_name','value_test')
while True:

    data = re.rpop("parkmsg")
    print(data)
    time.sleep(0.5)

