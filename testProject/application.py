from tornado.web import Application, StaticFileHandler
import config
from views.IndexHandler import IndexHandler
from views.InnerHandler import InnerHandler
from views.DetailHandler import DetailHandler
from views.HistoryHandler import HistoryHandler
from views.AboutHandler import AboutHandler
from views.ContactHandler import ContactHandler
from views.LoginHandler import LoginHandler
from views.RegisterHandler import RegisterHandler
from views.ReturnHandler import ResultHandler

class Applications(Application):
    def __init__(self):
        urls = [
            (r'/', IndexHandler),
            (r'/index/',IndexHandler),
            (r'/inner/(.*)$',InnerHandler),
            (r'/detail/',DetailHandler),
            (r'/history/',HistoryHandler),
            (r'/about/', AboutHandler),
            (r'/contact/', ContactHandler),
            (r'/login/', LoginHandler),
            (r'/reg/', RegisterHandler),
            (r'/result/(.*)$', ResultHandler),
        ]
        super(Applications, self).__init__(urls, **config.settings)