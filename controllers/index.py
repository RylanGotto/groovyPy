from tornado.web import RequestHandler
from routes import route
import tornado.websocket
import os
import local_search
import json
from player import con #controller
import thread
import time


print "Will not work with Internet Explorer use Chrome, or maybe firefox"
player_controller = con()


@route('/')
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        x = local_search.get_filepaths("C:\\\\users\\\\Rgott_000\\\\Music\\\\")
        self.render("index.html",x=x)

@route('/ws')
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        #thread.start_new_thread(self.playerloop, ())
        print "CONNECTED <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"

    def on_message(self, message):
        message = json.loads(message)
        res = player_controller.run(message)
        if res != None:
            self.write_message(json.dumps(res))
    def on_close(self):
        pass
   # def playerloop(self):
       # dict = {'type':'next_track','data':'workings'}
       # while True:
         #   time.sleep(2)
         #   if not player_controller.isplaying and not player_controller.paused:
            #    self.write_message(json.dumps(dict))


            
           




