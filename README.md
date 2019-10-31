# DataServiceLink
平台是 ubuntu16.04
python 版本是python3.5
开发环境是pycharm
这个是自己写的一个框架
主要功能就是
1、单线程接收tcpserver的数据
2、单线程添加数据进入redis
3、多线程消费，可以把redis的数据消费掉
4、modbus tcpclient的实现，可以写入到硬件中

使用redis的list实现数据缓存和消息队列功能
