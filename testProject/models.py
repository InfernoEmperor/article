from orm import orm

class Login(orm.ORM):
    def __init__(self,email,password):
        self.email = email
        self.passwd = password
        super(Login,self).__init__()
    def login(self):
        return self.Adjust(self.email,self.passwd)
        

class Registe(orm.ORM):
    def __init__(self,email,password,name,age = 18,introduce = ""):
        self.email = email
        self.passwd = password
        self.name = name
        self.age = age
        self.introduce = introduce
        super(Registe,self).__init__()

    
