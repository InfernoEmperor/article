from .dbMySql import SQL

class Record:
    def QueryRecord(self, email):
        sql = "select * from record where email='" + email + "'" 
        result = SQL().query(sql)
        return result
    def SetRecord(self, email, pic_1, pic_2, result):
        sql = "insert into record values('" + email + "','" + pic_1 + "','" + pic_2 + "','" + result+"')"
        return SQL().insert(sql)