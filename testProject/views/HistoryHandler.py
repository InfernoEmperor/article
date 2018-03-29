from tornado.web import RequestHandler
from orm.record import Record

class HistoryHandler(RequestHandler):
    def get(self, *args, **kwargs):
        #查询库，返回结果
        results = Record().QueryRecord(self.get_cookie('email'))
        objects = []
        for result in results:
            objects.append({
                "name" : result[0],
                "main" : result[1],
                "assist" : result[2],
                "result" : result[3],
            })
        self.render('history.html', objects = objects)
    def get_current_user(self):
        return self.get_cookie("user")