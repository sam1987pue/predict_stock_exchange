import numpy as np
import pandas as pd
from pandas_datareader import data, wb
import sys
import os

orig_stdout = sys.stdout
f = open('/home/linux/mercado valores/result.txt', 'w')
sys.stdout = f



with open('/home/linux/mercado valores/valores.volsa.txt') as e:
   for line in e:
        base_dir = '/home/linux/mercado \ valores/'
        

        fullpath = os.path.join(base_dir, line)
        

        data1 = pd.DataFrame.from_csv(fullpath)
    
        #data1 = pd.read_csv('/home/linux/Descargas/TL5.MC.csv')
    
        #data1.set_index('Date')
        #data1.info()
        #indexed_df = data1.set_index([[1]])
        #data1['Close'].plot(grid=True, figsize=(8, 5))
        
        data1['42d'] = np.round(pd.rolling_mean (data1 ['Close' ], window =42), 2)
        
        data1['252d'] = np.round(pd.rolling_mean (data1 ['Close' ], window =252), 2)
        
        #data1 [['Close' , '42d' , '252d' ]].tail()
        
        data1[['Close', '42d', '252d']].plot(grid=True, figsize =(8, 5))


sys.stdout = orig_stdout

f.close()
      
        



