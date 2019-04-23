# -*- coding: utf-8 -*-
#version:ython 2.7
#create time:14:17 2019-04-22
#update time:
#author:cwq


import tornado.ioloop
import tornado.web
from tornado import gen
import time
import tornado.options
from tornado.httpserver import HTTPServer

tornado.options.define('port',default=8888,type=int,help="this is the port for application")



class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        from tornado import httpclient
        http = httpclient.AsyncHTTPClient()
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        yield http.fetch("http://127.0.0.1:8888/index", self.done)


    
    def done(self, *args, **kwargs):
        print ("start done function")
        time.sleep(3)
        self.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        self.finish()


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("林舒卿，我中意你!!!")


application = tornado.web.Application([
    (r"/main", MainHandler),
    (r"/index", IndexHandler),
],debug=True)

if __name__ == "__main__":
    print "start web sever!!!"
    tornado.options.parse_command_line()
    http_server = HTTPServer(application)
    http_server.bind(tornado.options.options.port)
    http_server.start(1)
    #启动IOLoop轮循监听
    tornado.ioloop.IOLoop.current().start()
