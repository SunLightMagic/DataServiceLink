
import pymysql
import datetime
class Sqlquery():
    def __init__(self):
        self.dbname='test'
        self.host='62.234.105.77'
        self.port=3306
        self.usrname='king'
        self.passwd='Zsj20122766'
        self.conn=pymysql.connect(host=self.host,port=self.port, user=self.usrname,
            passwd=self.passwd, db=self.dbname, charset='utf8')

    def select_all(self,pkarea):
        sqlstr='select allnum from areainfo where parkarea=%s;'%(pkarea)
        cursor=self.conn.cursor()
        cursor.execute(sqlstr)
        data=cursor.fetchone()
        print('allnum:',data[0])
        return ord(data[0])
    def select_free(self,pkarea):
        str='select freenum from areainfo where parkarea=%s;'%(pkarea)
        cursor=self.conn.cursor()
        cursor.execute(str)
        data=cursor.fetchone()
        print('freenum:',data[0])
        return ord(data[0])
'''
if __name__ == "__main__":
    query = Sqlquery()
    query.select_all('1')
    query.select_free('1')
'''