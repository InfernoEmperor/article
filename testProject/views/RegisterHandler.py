from tornado.web import RequestHandler
from models import Registe

class RegisterHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('reg.html',str = None)

    def post(self, *args, **kwargs):
        email = self.get_argument('email')
        
        passwd = self.get_argument('password1')
        npasswd = self.get_argument('password2')
        
        name = self.get_argument('name')
        age = self.get_argument('age','18')
        age = int(age)
        introduce = self.get_argument('introduce','')
        reg = Registe(email,passwd,name,age,introduce)
        if reg.Insert() > 0:
            self.redirect('/login/')
        elif not Registe.delrewrite(email):
            self.render('reg.html',str = '邮箱已注册')
        elif passwd != npasswd:
            self.render('reg.html',str = '请重新输入，确保两次密码一致')
        else:
            self.render('reg.html',str = '注册失败，请联系管理员')
