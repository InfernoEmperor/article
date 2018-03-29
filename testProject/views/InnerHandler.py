from tornado.web import RequestHandler
from .indexContent.content import imgs

class InnerHandler(RequestHandler):
    def get(self, *args, **kwargs):
        content = {}
        res = self.get_argument('name',None)
        if res is None:
            content = {
                'name' : '',
                'title' : '',
                'content' : ''
            }
        for img in imgs:
            if img['name'] == res:
                content = img
                break
        self.render('inner.html', content = content)
    def get_current_user(self):
        return self.get_cookie("user")

        