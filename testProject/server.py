import tornado.ioloop
import tornado.httpserver
import config
from application import Applications

if __name__ == "__main__":
    app = Applications()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(config.options.get('port'))
    tornado.ioloop.IOLoop.current().start()