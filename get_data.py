import requests
import json
import pandas as pd
from pandas import ExcelWriter
from pytrends.request import TrendReq
from datetime import timedelta, datetime
from random import randrange
import time

def get_data_from_coinapi():
	url = 'https://rest.coinapi.io/v1/orderbooks//history?time_start=2018-01-01T00:00:00&limit=10'
	headers = {'X-CoinAPI-Key' : '63BC9096-979E-4855-8A91-B84E310F37FE'}
	response = requests.get(url, headers=headers)
	json_data = response.json()
	print(json_data)
	data_df = pd.read_json(json_data)
	print(data_df)
	return data_df

def get_ripple_data():
	limit = '20000'
	json_format = "json"
	csv_format = "csv"
	start_date = "2016-05-01T12:00:00Z"
	end_date = "2018-05-20T12:00:00Z"
	origin_json_url = "https://data.ripple.com/v2/exchanges/USD+rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q/XRP?descending=false&limit="+limit+"&result=tesSUCCESS&type=OfferCreate&interval=1minute&start="+start_date+"&format="+json_format+"&end="+end_date
	origin_csv_url = "https://data.ripple.com/v2/exchanges/USD+rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q/XRP?descending=false&limit="+limit+"&result=tesSUCCESS&type=OfferCreate&interval=1minute&start="+start_date+"&format="+csv_format+"&end="+end_date
	
	response = requests.get(origin_json_url)
	json_data = response.json()

	data_df = pd.read_csv(origin_csv_url)
	
	#print(json_data)
	marker = json_data["marker"]

	while True:
		print(marker)
		response = requests.get(origin_json_url+"&marker="+marker)
		json_data = response.json()
		
		if 'marker' in json_data:
			if marker == json_data["marker"]:
				# end of file 
				print('---------end---------')
				break
			else:
				next_batch_df = pd.read_csv(origin_csv_url+"&marker="+json_data["marker"])
				data_df = data_df.append(next_batch_df)
				marker = json_data["marker"]
		else:
			break

	writer = pd.ExcelWriter("Ripple_Minute_Historical_Data_since_2016.xlsx",  engine='xlsxwriter')
	data_df.to_excel(writer)
	writer.save()

	return data_df

#get_ripple_data()

def get_google_trends():
	keywords = ["Bitcoin, Ethereum, Ripple"] 

	# pytrends = TrendReq(proxies="{'http': 'http://192.168.0.1:8887'}")

	start_date = datetime.strptime('2015-01-06T00', '%Y-%m-%dT%H')
	end_date = datetime.strptime('2015-01-13T23', '%Y-%m-%dT%H')
	#start_date = datetime.strptime('2017-12-12T00', '%Y-%m-%dT%H')
	#end_date = datetime.strptime('2017-12-19T23', '%Y-%m-%dT%H')
	delta = timedelta(days=8)
	time_now = datetime.now()

	df = pd.DataFrame()
	pytrends = TrendReq( hl='en-US', tz=0, geo='', proxies={ 'https': 'https://52.87.245.237:3128' })

	writer = pd.ExcelWriter("CryptoGoogleTrends.xlsx",  engine='xlsxwriter')

	while True:
		

		if (end_date > time_now):
			break

		start_date_str = start_date.strftime('%Y-%m-%dT%H')
		end_date_str = end_date.strftime('%Y-%m-%dT%H')
		tf = start_date_str + ' ' + end_date_str
		try:
			print('entered try')
			pytrends.build_payload(kw_list=["Bitcoin", "Ethereum", "Bitstamp", "Buy Bitcoin", "Coinbase"], timeframe=tf)
			print('built payload')
			interest_over_time_df = pytrends.interest_over_time()
			print(interest_over_time_df.head())
			print(interest_over_time_df.tail())
			df = df.append(interest_over_time_df)
			print("not exception")
			
			start_date += delta
			end_date += delta 
			df.to_excel(writer)
		except Exception as e:
			print(e)
			pass
		
		print('exited try/except')

	
	writer.save()

get_google_trends()