import _thread
import time
def print_time(threadname,delaytime):
    count=0
    while count<10:
        time.sleep(delaytime)
        count+=1
        print("%s: %s" % (threadname, time.ctime(time.time())))
try:
    _thread.start_new_thread(print_time,("thread_1",1,))
    _thread.start_new_thread(print_time,("thread_2",2,))
except:
    print("error!")

while 1:
    pass