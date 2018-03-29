import pymysql
import config

def singleton(cls,*args,**kwargs):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return _singleton

@singleton
class SQL:
    host = config.database['host']
    port = config.database['port']
    user = config.database['user']
    passwd = config.database['passwd']
    dbName = config.database['dbName']
    
    def __connect(self):
        self.db = pymysql.connect(host = self.host,port = self.port,user = self.user,passwd = self.passwd,db = self.dbName,charset = 'utf8')
        self.cursor = self.db.cursor()
    def __close(self):
        self.cursor.close()
        self.db.close()

    def query(self,sql):
        self.__connect()
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        self.__close()
        return res
    def all(self,sql):
        self.__connect()
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        self.__close()
        return res
    def __exec(self,sql):
        count = 0
        try:
            self.__connect()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.__close()
        except:
            self.db.rollback()
        finally:
            return count    #表示影响行数

    def insert(self,sql):
        return self.__exec(sql)

    