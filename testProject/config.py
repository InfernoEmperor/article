import os
BASE_DIRS = os.path.dirname(__file__)

options = {
    'port' : 8888
}

settings = {
    'static_path' : os.path.join(BASE_DIRS,"static"),
    'template_path' : os.path.join(BASE_DIRS,'templates'),
    'debug' : False,
}

database = {
    "host" : "127.0.0.1",
    'port' : 3306,
    "user" : "root",
    'passwd' : '111111',
    'dbName' : 'pictures',
}

cache = {
    "host" : "127.0.0.1",
    "port" : "6666"

}