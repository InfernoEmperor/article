from tornado.web import RequestHandler

class ContactHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('contact.html')
    def get_current_user(self):
        return self.get_cookie("user")