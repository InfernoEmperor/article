import redis
import config
import time

class OperateRedis:
    def __init__(self):
        self.conn = redis.Redis(config.cache.get('host'), config.cache.get('port'))
    
    def Set(self, email, strID):
        if self.conn.set(email, strID) is None:
            print("redis设置值失败！")

    def Get(self, email):
        strM = self.conn.get(email).decode("utf-8")
        self.conn.delete(email)
        return strM


