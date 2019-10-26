import sys
import billboard
scope = 'user-library-read'
song_names = []

chart = billboard.ChartData('hot-100')
print(type(chart))
print(len(chart))

#print (chart)

song = chart[0]
#print(song.title) - Truth Hurts
#print(song.artist) - Lizzo

print(type(song.title))



'''
def songs_from_chart(chart):
	song = []
	for i in chart:
		song
'''

def dict_from_chart(chart,dictionary):
	for i in range (len(chart)):
		song = chart[i]
		#print(song.title)
		#print(dictionary.keys())
		if not song.title in dictionary.keys():
			dictionary[song.title] = ''

	return dictionary

dictionary = {}
print(dict_from_chart(chart,dictionary))










