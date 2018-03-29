from tornado.websocket import  WebSocketHandler
from orm.redis import OperateRedis 

class ResultHandler(WebSocketHandler):
    users = {}
    def open(self, *args, **kwargs):
        email = self.get_argument('email')
        if email is not "":
            if email not in self.users:
                self.users[email] = self
            self.write_message("1," + "我们正在为您处理！产生结果会通知您！")
            
    
    def on_message(self,message):
        if message == "query":
            strName = OperateRedis().Get(self.get_cookie('email'))
            if strName is not None:
                s = "http://127.0.0.1:8888/static/upfile/" + strName
                self.write_message("2," + s)
            else:
                self.write_message("1," + "服务器错误！")    
          
        
    
    def check_origin(self,origin):
        return True    
    
    def on_close(self):
        for email in self.users:
            if self.users[email] == self:
                ResultHandler.users.pop(email)
                break