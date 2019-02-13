#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 23:14:06 2018

@author: linux
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import glob


files = glob.glob('/home/linux/mercadovalores/nasdaqhistoric/historic/historic.22.06/*_2TR.csv')

for line in files:
   #base_dir = "/home/linux/mercadovalores/"

   #orig_stdout = sys.stdout
   #f = open('results.odt', 'w')
   #sys.stdout = f

   #fullpath = os.path.join(base_dir, line)

   data1 = pd.DataFrame.from_csv(line)

 
   data1[['close', '42d', '252d']].plot(grid=True, figsize =(8, 5))

   plt.savefig(line+'_2TR.png')  