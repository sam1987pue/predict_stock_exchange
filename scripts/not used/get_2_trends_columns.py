
"""
Created on Fri Mar 16 21:44:22 2018

@author: linux
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import glob


files = glob.glob('/home/linux/mercadovalores/nasdaqhistoric/historic/historic.22.06/*.csv')

for line in files:
   #base_dir = "/home/linux/mercadovalores/"

   #orig_stdout = sys.stdout
   #f = open('results.odt', 'w')
   #sys.stdout = f

   #fullpath = os.path.join(base_dir, line)

   data1 = pd.DataFrame.from_csv(line)
   
   data1['42d'] = np.round(pd.rolling_mean (data1 ['close' ], window =42), 2)
    
   data1['252d'] = np.round(pd.rolling_mean (data1 ['close' ], window =252), 2)
    
    #data1 [['Close' , '42d' , '252d' ]].tail()
   data1.to_csv(line+'2TR.csv')
 
