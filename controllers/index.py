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
        x = local_search.get_filepaths("/home/rylan/Music")
        self.render("index.html",x=x)

@route('/ws')
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        thread.start_new_thread(self.playerloop, ())

    def on_message(self, message):
        message = json.loads(message)
	print message
        player_controller.run(message)

    def on_close(self):
        player_controller.player.stop()
    def playerloop(self):
        dict = {'type':'next_track','data':'workings'}
        while True:
            time.sleep(3)
            if not player_controller.isplaying and not player_controller.paused:
		print "should be sending out msg now!"
                self.write_message(json.dumps(dict))


            
           




