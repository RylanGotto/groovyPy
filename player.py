import groovewrap
import mplayer
import thread
import time
import os
from subprocess import Popen, PIPE
import subprocess


<<<<<<< HEAD
=======
class con(object):
	def __init__(self):
		self.player = mplayer.Player()
		self.paused = False
		self.isplaying = None
		thread.start_new_thread(self.is_playing, ())
		
	def run(self, message):
				if message['type'] == 'song':
						self.player.stop()
						self.player.loadfile(message['data'])
						self.paused = False
						self.isplaying = True
				if message['type'] == 'pause':
					if not self.paused:
						self.player.pause()
						self.paused = True
						self.isplaying = False						
					else:	
						self.player.pause()
						self.paused = False
						self.isplaying = True
				if message['type'] == 'next':
						pass
				if message['type'] == 'volume':
						time.sleep(0.1)
						print message['data']
						self.player.volume = message['data']
	            		

						
	def is_playing(self):
		while True:
			while self.player.time_pos != self.player.time_pos:
				time.sleep(1)
				self.isplaying = True
				print self.isplaying
			else:
				print self.isplaying
				if self.paused is True:
					self.isplaying = True
				else:
					self.isplaying = False

			
					


				
			
>>>>>>> 1e5b80a81e029b70f49e01ace4b17f45df9c55d0


class con(object):

    def __init__(self):
        pass
        #thread.start_new_thread(self.is_playing, ())

    def run(self, message):
        os.system("taskkill /F /im  mplayer.exe")
        self.player = mplayer.Player()
        self.paused = False
        self.isplaying = None
        self.process = None
        time.sleep(0.01)
        if message['type'] == 'song':
            try:
                if isinstance(int(message['data']), int):
                    vv = "http://api.soundcloud.com/tracks/%s/stream?client_id=3ad50aa94ca89d3326523ad065bcfee7" % str(
                        message['data'])
                    print "here"
                    if self.process != None:
                        self.process.terminate()
                        self.process = Popen(["mplayer", vv], stdout=PIPE)
                        self.player.pause()
                        self.paused = False
                        self.isplaying = False

                    else:
                        self.process = Popen(["mplayer", vv], stdout=PIPE)
                        self.player.pause()
                        self.paused = False
                        self.isplaying = False
            except:
                if self.process != None:
                    self.process.terminate()
                    self.process = None
                    s = message['data'].replace('\\\\', '\\')
                    self.player.loadfile(s)
                    self.player.pause()
                    self.paused = False
                    self.isplaying = True
                else:
                    vv =  message['data']
                    print "here"
                    if self.process != None:
                        self.process.terminate()
                        self.process = Popen(["mplayer", vv], stdout=PIPE)
                        self.player.pause()
                        self.paused = False
                        self.isplaying = False

                    else:
                        self.process = Popen(["mplayer", vv], stdout=PIPE)
                        self.player.pause()
                        self.paused = False
                        self.isplaying = False
                    self.paused = False
                    self.isplaying = True
        if message['type'] == 'pause':
            if not self.paused:
                self.player.pause()
                self.paused = True
                self.isplaying = False
            else:
                self.player.pause()
                self.paused = False
                self.isplaying = True
        if message['type'] == 'next':
            pass
        if message['type'] == 'volume':
            time.sleep(0.1)
            self.player.volume = message['data']
        if message['type'] == 'search':
            gs_results = groovewrap.get_gsresults(message['data'])
            response = {'type': 'gs_response', 'data': gs_results}
            return response

    # def is_playing(self):
        # while True:
                    # time.sleep(1)
                    # while self.player.time_pos != self.player.time_pos:
                    #	time.sleep(1)
                    #	self.isplaying = True
                    # else:
        # if self.paused is True:
        #	self.isplaying = True
        # else:
        #	self.isplaying = False
