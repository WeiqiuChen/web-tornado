# -*- coding: utf-8 -*-
#version:ython 2.7
#create time:14:17 2019-04-22
#update time:
#author:cwq


import tornado.ioloop
import tornado.web
from tornado import gen
class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        import time
        self.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Index!!!")

application = tornado.web.Application([
    (r"/main", MainHandler),
    (r"/index", IndexHandler),
])

if __name__ == "__main__":
    print "start web sever!!!"
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()