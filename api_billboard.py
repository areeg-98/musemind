import sys
import billboard
import datetime
import pandas as pd
import csv


start_date = '2015-04-25'
chart = billboard.ChartData('hot-100', start_date)
#print(chart)
#print(type(chart.previousDate))
#print(datetime.strptime(chart.previousDate))

#print(type(song.title)) - str

#while chart.previousDate:

total_chart = []
total_chart.append(chart)
print(total_chart)

for i in range(5):
    chart = billboard.ChartData('hot-100', chart.previousDate)
    total_chart.append(chart)

print(total_chart)



def dict_from_chart(chart,dictionary):
	for i in range (len(chart)):
			song = chart[i]
			if not song.title in dictionary.keys():
				dictionary[song.title] = ''

	return dictionary


def dict_from_total_chart(total_chart,dictionary):
	for chart in total_chart:
		for i in range (len(chart)):
			song = chart[i]
			#print(song.title)
			#print(dictionary.keys())
			if not song.title in dictionary.keys():
				dictionary[song.title] = ''

	return dictionary

dictionary = {}
#print(dict_from_chart(chart,dictionary))
dict_from_total_chart(total_chart,dictionary)
print(len(dictionary))

#df = pd.DataFrame(dictionary,index=[0])
#df.to_csv("billboard_data.csv")
with open('billboard_data_7.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, dictionary.keys())
    w.writeheader()
    w.writerow(dictionary)










