import pandas as pd
import os

#files = os.listdir()[1:-1]

csv_file=input('csv_file file name\n : ')+'.csv'

def filter(csv_file):
	data = pd.read_csv(csv_file)

	fields=[
	'url',
	'organicResults/0/description',
	'organicResults/0/title',
	'organicResults/0/url',
	'organicResults/1/description',
	'organicResults/1/title',
	'organicResults/1/url',
	'organicResults/2/description',
	'organicResults/2/title',
	'organicResults/2/url',
	'organicResults/3/description',
	'organicResults/3/title',
	'organicResults/3/url',

	'organicResults/4/description',
	'organicResults/4/title',
	'organicResults/4/url',

	'organicResults/5/description',
	'organicResults/5/title',
	'organicResults/5/url',

	'organicResults/6/description',
	'organicResults/6/title',
	'organicResults/6/url',

	'organicResults/7/description',
	'organicResults/7/title',
	'organicResults/7/url',

	'organicResults/8/description',
	'organicResults/8/title',
	'organicResults/8/url',

	'organicResults/9/description',
	'organicResults/9/title',
	'organicResults/9/url'
	]
	data.reindex(columns=fields).to_csv(f'filtered_{csv_file}', index=False)

filter(csv_file)
#for ecsv in files:
#	filter(ecsv)
