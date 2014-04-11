from grooveshark import Client
import soundcloud
import time
def get_gsresults(searchterms):
	c = Client()
	c.init()
	d = c.search(searchterms)
	x = 0
	v = 0
	client = soundcloud.Client(client_id='dcc1e7da1893fe098685ba22946454eb')
	tracks = client.get('/tracks', q=searchterms, license='cc-by-sa')
	r = []
	for i in tracks.data:
		 if x < 10:
			 r.append({'artist':i.user['username'], 'title':i.title, 'url':i.id, 'arturl':i.artwork_url})
			 x += 1
			 continue
		 for i in d:
			 if v < 10:
				 r.append({'album':i._album_name, 'artist':i._artist_name, 'title':i.name, 'url':i.stream.url, 'arturl':i._cover_url})
				 v += 1
			
	return r



		 	
	
