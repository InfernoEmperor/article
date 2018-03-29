from tornado.web import RequestHandler

class AboutHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('about.html')
    def get_current_user(self):
        return self.get_cookie("user")    