import sys
import billboard
import datetime

chart = billboard.ChartData('hot-100')
print(type(chart.previousDate))
#print(datetime.strptime(chart.previousDate))

#print(type(song.title)) - str

#while chart.previousDate:

total_chart = []
total_chart.append(chart)
print(total_chart)

for i in range(3):
    chart_1 = billboard.ChartData('hot-100', chart.previousDate)
    total_chart.append(chart_1)

print(total_chart)




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










