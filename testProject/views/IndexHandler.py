from tornado.web import RequestHandler
from .indexContent.content import imgs

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html',imgs = imgs)
    def get_current_user(self):
        return self.get_cookie("user")

        