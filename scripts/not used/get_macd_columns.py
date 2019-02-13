#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 15:45:47 2018

@author: linux
"""

import pandas as pd
from stockstats import StockDataFrame
import matplotlib.cbook as cbook
import glob



files = glob.glob('/home/sam/csv_files/*.csv')

for line in files:
    
    fname = cbook.get_sample_data(line, asfileobj=False)

    df = StockDataFrame.retype(pd.read_csv(fname))




    df['macd'] = df.get('macd') # calculate MACD
    df['rsi_6'] = df.get('rsi_12')
    df['kdjk'] = df.get('kdjk')
#df['42d'] = np.round(pd.rolling_mean (df['close' ], window =42), 2)
#df['252d'] = np.round(pd.rolling_mean (df['close' ], window =252), 2)

#print df.head()

    filename = df.to_csv(line+'_macd.csv')
    
       
        


#print df

    
    #data1 [['Close' , '42d' , '252d' ]].tail()
    
   #data1[['close', '42d', '252d']].plot(grid=True, figsize =(8, 5))

   #plt.savefig(line+'.png')  

#df['macd'] = df.get('macd') # calculate MACD






#df[['close','macds', 'macd']].plot(grid=True, figsize =(8, 5))