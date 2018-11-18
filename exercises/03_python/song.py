import json

class Song:
	def __init__(self, some_song):
		
		file_directory = "lastfm_subset/"+ some_song[2] + "/" + some_song[3] + "/" + some_song[4] + "/" + some_song + ".json"
		with open(file_directory) as json_data:
			data = json.load(json_data)
		
		
			self.artist = data["artist"]
			self.title = data["title"]
			self.timestamp = data["timestamp"]
			self.similars = data["similars"]
			self.tags = data["tags"]
			self.track_id = data["track_id"]
		
	def get_tags(self, limit=None):
		tag_list = []
		if limit is None:
			for tag in self.tags:
				tag_list.append(tag[0])
		else:
			for tag in self.tags:
				if limit <= int(tag[1]):
					tag_list.append(tag[0])
		return tag_list
			
				
				
				
	def get_similars(self,limit=None):
		track_list = []
		if limit is None:
			for tracks in self.similars:
				track_list.append(tracks[0])
		else:
			for tracks in self.similars:
				if limit <= tracks[1]:
					track_list.append(tracks[0])
		return track_list
		
	def shared_tags(self, some_song):
		myTags = self.get_tags()
		myTuple = ()
		for tags in some_song.get_tags():
			if tags in myTags:
				myTuple = myTuple + (tags,)
		return myTuple
					
	
	def combined_tags(self, some_song):
		myTags = self.get_tags()
		mySet = set()
		for tags in some_song.get_tags():
			mySet.add(tags)
		for tags in self.get_tags():
			mySet.add(tags)
		return mySet