from tornado.web import RequestHandler
from models import Login

class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html',flag = None)
    def post(self):
        account = self.get_body_argument('email')
        password = self.get_body_argument('password')
        login = Login(account,password)
        if login.login():
            url = '/detail/'
            name = login.emailToname(account)[0][0]
            self.set_cookie("user", name)
            self.set_cookie('email', account)
            self.redirect(url)
        else:
            self.render('login.html',flag = True)