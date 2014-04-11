import os
import re


def get_filepaths(directory):

	file_paths = {}
	for root, directories, files in os.walk(directory):
		for filename in files:
			extension = filename.lower()
			if extension.endswith('.mp3') or extension.endswith('.m4a') or extension.endswith('.aac') or extension.endswith('.ogg') or extension.endswith('.mp4'):
				filepath = os.path.join(root, filename)
				filepath = filepath.replace('\\\\', '\\') #if any one ever has to maintain this, I am sorry just know this is because the path is being dumped 
														  #so many times it will keep losing a back slash on windows, :( fuck windows
				filepath = filepath.replace('\\', '\\\\')
				file_paths.update({filepath:filename})
	return file_paths

def search_filenames(terms, directory):
	pathResults = {}
	result = []
	paths = []
	mp3s = get_filepaths(directory)
	user_terms = get_user_terms(terms)
	for key, value in mp3s.items():
		dir_terms = get_dir_terms(value)
		
		for usrword in user_terms:
			for dirword in dir_terms:
				if usrword == dirword and value not in result:
					result.append(value)
					paths.append({'path':key, 'title':value})
	pathResults.update({'data':paths})
	return pathResults

def get_dir_terms(filename):
	filename = filename.lower()
	pattern = re.compile('[\W\d]+')
	dir_terms = pattern.sub(' ',filename)
	return dir_terms.split(" ")

def get_user_terms(srch_str):
	userCompWords = srch_str.lower().split(" ") #User Comparable words
	return userCompWords





