from .dbMySql import SQL

class ORM:
    def Insert(self):
        try:
            cls_name = (self.__class__.__name__).lower()
            if cls_name == 'registe':
                sql = "insert into users values("
                for field in self.__dict__:
                    if isinstance(self.__dict__[field],str):
                        sql += "'" + self.__dict__[field] + "',"
                    else:
                        sql += str(self.__dict__[field]) + ","
                sql = sql[:len(sql) - 1] + ")"

                db = SQL()
                return db.insert(sql)
            else:
                return 0
        except Exception as e:
            print('异常',e)
            return 0

    def Adjust(self,email,password):
        cls_name = (self.__class__.__name__).lower()
        if cls_name == 'login':
            sql = "select * from users where email='"+ email +"' and " + "passwd='" + password + "'"
            #print(sql)
            db = SQL()
            return db.query(sql)


    @classmethod
    def getDetail(cls,email):
        sql = "select name,age,introduce from users where email='"+ email +"'"
        db = SQL()
        return db.all(sql)
    @classmethod
    def delrewrite(cls,email):
        sql = "select * from users where email='"+ email +"'"
        db = SQL()
        return  False if len(db.query(sql)) > 0 else True

    @classmethod
    def emailToname(cls,email):
        sql = "select name from users where email='"+ email +"'"
        db = SQL()
        return db.query(sql)

