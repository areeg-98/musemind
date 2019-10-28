import sys
import billboard
import datetime
import pandas as pd
import csv


#print(billboard.charts())

start_date = '2019-02-16'
chart = billboard.ChartData('emerging-artists', start_date)
print(chart)
print(len(chart))
print(chart[0])
#print(type(chart.previousDate))
#print(datetime.strptime(chart.previousDate))

#print(type(song.title)) - str

#while chart.previousDate:

#total_chart = []
#total_chart.append(chart)
#print(total_chart)

#for i in range(5):
 #   chart = billboard.ChartData('hot-100', chart.previousDate)
  #  total_chart.append(chart)

#print(total_chart)



def dict_from_chart(chart,dictionary):
	for i in range (len(chart)):
			song = chart[i]
			if not song in dictionary.keys():
				dictionary[song] = ''

	return dictionary



dictionary = {}
print(dict_from_chart(chart,dictionary))
#dict_from_total_chart(total_chart,dictionary)
print(len(dictionary))



#df = pd.DataFrame(dictionary,index=[0])
#df.to_csv("billboard_data.csv")
with open('emerging_artists.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, dictionary.keys())
    w.writeheader()
    w.writerow(dictionary)











