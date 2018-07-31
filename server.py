import tornado.ioloop
import tornado.web
from wordapi.controller import *


application = tornado.web.Application([
    (r"/", HomePageController),
    (r"/website", WebsiteController),
    (r"/admin", AdminController),
])

if __name__ == "__main__":
    application.listen(8888, address='0.0.0.0')
    tornado.ioloop.IOLoop.instance().start()