import csv
import pandas as pd


my_csv = pd.read_csv('featuresdf.csv')
print(my_csv)
print(my_csv['name'])
print(type(my_csv['name']))
my_csv['name'].to_csv('top_2017_names.csv')

