# -*- coding: utf-8 -*-"""
import os
from mutagen.easyid3 import EasyID3



def is_valid_filename(song):
	for letter in song:
		if ord(letter) == 63 or ord(letter) > 125:
			return False
	return True

def is_valid_date(date):
	return date != -1 and len(date[0]) == 4

def is_valid_length(length):
	return length != -1

def average_dates(lst):
	sum = 0
	count = 0
	if len(lst) == 0:
		return "No songs were processed"
	else:
		for item in lst:
			item = float(item[0])
			sum += item
			count += 1
		print str(count) + " songs processed."
		avg = sum/count
		return int(round(avg))

def average_lengths(lst):
	sum = 0
	count = 0
	if len(lst) == 0:
		return "no songs were processed"
	else:
		for item in lst:
			item = float(item)
			sum += item
			count += 1
		avg = sum/count
		return int(round(avg))

def songlist(directory):

	os.chdir(directory)

	songlist = []

	for root, dirs, files in os.walk(directory):
	    for file in files:
	        if file.endswith(".mp3"):
	        	path = os.path.join(root, file)
	        	songlist.append(path)
	return filter(is_valid_filename, songlist) #filter out any invalid song names (e.g. files with special characters - ascii only!)


def datelist(songlist):
	datelist = []
	count = 0
	for song in songlist: #build the list of dates
		count += 1
		song = EasyID3(song)
		date = song.get('date', -1)
		datelist.append(date)

	return filter(is_valid_date, datelist) #filter out invalid dates, or void dates

def tracknumlist(songlist):
	tracknumlist = []
	count = 0
	for song in songlist: #build the list of dates
		count += 1
		song = EasyID3(song)
		date = song.get('tracknumber', -1)
		tracknumlist.append(date)

	return tracknumlist #filter out invalid dates, or void dates

def lengthlist(songlist):
	lengthlist = []
	count = 0
	for song in songlist: #build the list of dates
		count += 1
		song = EasyID3(song)
		length = song.get('length', -1)
		lengthlist.append(length)
	print count
	return filter(is_valid_length, lengthlist) #filter out invalid dates, or void dates
#----------------------------------------------------------------
directory = r"D:\Music\Frank Zappa"
print EasyID3.valid_keys.keys()
songlist = songlist(directory) #get the list of songs

for song in songlist:
	song = EasyID3(song)
	print song['length']

datelist = datelist(songlist)
#tracknumlist = tracknumlist(songlist)
lengthlist = lengthlist(songlist)
print lengthlist

print average_dates(datelist) # print that shit
print average_lengths(lengthlist)

# to do:
# track might be 2, 02, 2/<album length>, write function to get the correct value (2) from it