
import requests
"""takes json object from server,
 breaks it down into separate componants, 
 returns dicts of youtube video information

 Michael McCulloch"""
class youtube_wrap:
	def __init__(self, search):
		self.searchterms = search
		self.payload = {'searchterms':self.searchterms}
		self.json_response = requests.get("http://iamrylangotto.com:8000", params=self.payload).json()

		self.vidID = []
		self.tits = []
		self.thumbs = []
		self.desc = []

		self.json_Strip()

	def json_Strip(self):
		for search_result in self.json_response.get('items',[]):
			self.vidID.append(search_result['id']['videoId'])
			self.tits.append(search_result['snippet']['title'])
			self.thumbs.append(search_result['snippet']['thumbnails']['medium']['url'])
			self.desc.append(search_result['snippet']['description'])

	def get_everything(self):
		array = []
		for i in range(len(self.vidID)):
			array.append({'vidid': self.vidID[i], 'title': self.tits[i], 'thumbs': self.thumbs[i], 'desc': self.desc[i]})
		return array