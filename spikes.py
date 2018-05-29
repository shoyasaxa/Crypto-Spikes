import pandas as pd 
import matplotlib.pyplot as plt
from pandas import ExcelWriter


def split_excel_file(file_name):
	df = pd.read_csv(file_name)

	writer = pd.ExcelWriter("BTC-part1.xlsx",  engine='xlsxwriter')
	df[:len(df)/2].to_excel(writer)
	writer.save()

	writer2= pd.ExcelWriter("BTC-part2.xlsx", engine='xlsxwriter')
	df[len(df)/2+1:].to_excel(writer2)
	writer2.save()

	return 

def analyze(file_name):
	df = pd.read_csv(file_name)

	df[:len(df)/2]

	fig, ax = plt.subplots()
	ax.plot(df["Timestamp"], df["Close"])
	ax.set_title("Bitcoin since 2012")
	ax.set(ylabel="price",xlabel="time")
	plt.show()
	return 


def main():
	#analyze('../data/BTC/BTC_2012-2018_1min.csv')
	split_excel_file('../data/BTC/BTC_2012-2018_1min.csv')

