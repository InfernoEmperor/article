from tornado.web import RequestHandler
import uuid
from orm.redis import OperateRedis
from orm.record import Record
import multiprocessing
from machine_learning.Interface import Deal

class DetailHandler(RequestHandler):
    def get(self, *args, **kwargs):
        user = self.get_cookie('user', None)
        if user is None:
            self.redirect('/login/')
        else:
            self.render('main.html')
    def post(self):
        files = self.request.files.get('fileselect')
        id = []
        for img in files:
            id.append(uuid.uuid3(uuid.NAMESPACE_OID, img['filename']))
            with open('./static/upfile/'+ str(id[-1]) +'.jpg','wb') as f:
                f.write(img['body'])
            user = self.get_current_user()
        #调用机器学习模型  记录存入sql中，待结果出来后通过websocket返回
        #另起一个进程
        multiprocessing.Process(target=Deal, args=(self.get_cookie('email'), id[0], id[1])).start()
        
        self.render('result.html')
    def get_current_user(self):
        return self.get_cookie("user")