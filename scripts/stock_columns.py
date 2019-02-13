import numpy as np
import pandas as pd
import glob
from stockstats import StockDataFrame
import matplotlib.cbook as cbook
import csv



files = glob.glob('*.csv')



class get_more_columns:


  def get_2TR_csv(self):
	global files
	for line in files:
		data1 = pd.DataFrame.from_csv(line)
		close = data1['close' ]
		data1['42d'] = np.round(close.rolling(42).mean())
		data1['252d'] = np.round(close.rolling(252).mean())
		data1.to_csv('TR_'+line)

  def get_stocks_columns(self):

	global files
	for line in files:
		fname = cbook.get_sample_data(line, asfileobj=False)
		fname = fname[71:]
		print fname
		df = StockDataFrame.retype(pd.read_csv(fname))
		df['macd'] = df.get('macd') # calculate MACD
		df['rsi_6'] = df.get('rsi_12')
		df.to_csv(line)



def main():
	column = get_more_columns()
	column.get_2TR_csv()
	column.get_stocks_columns()

if  __name__ =='__main__':
    main()
