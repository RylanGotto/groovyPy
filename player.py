import mplayer
import thread
import time
import os

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
						self.player.volume = message['data']
						
	def is_playing(self):
		while True:
			while self.player.time_pos != self.player.time_pos:
				time.sleep(1)
				self.isplaying = True
			else:
				if self.paused is True:
					self.isplaying = True
				else:
					self.isplaying = False

			
					


				
			







