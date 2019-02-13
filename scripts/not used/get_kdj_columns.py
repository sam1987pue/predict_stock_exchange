#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 16:35:09 2018

@author: linux
"""
import pandas as pd
from stockstats import StockDataFrame
import matplotlib.cbook as cbook
import glob



files = glob.glob('/home/linux/mercadovalores/nasdaqhistoric/historic/historic.25.05/follow/*_macd.csv_last.csv')

for line in files:
    
    fname = cbook.get_sample_data(line, asfileobj=False)

    df = StockDataFrame.retype(pd.read_csv(fname))

    df['kdjk'] = df.get('kdjk') # calculate MACD
#df['42d'] = np.round(pd.rolling_mean (df['close' ], window =42), 2)
#df['252d'] = np.round(pd.rolling_mean (df['close' ], window =252), 2)

#print df.head()

    filename = df.to_csv(line+'_kdj.csv')