#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May  5 20:12:41 2018

@author: linux
"""

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import glob


files = glob.glob('/home/linux/mercadovalores/nasdaqhistoric/historic/historic.22.06/*.csv_macd.csv_last.csv')

for line in files:
    print line

    faname = cbook.get_sample_data(line, asfileobj=False)
    
    plt.style.use("Solarize_Light2")
    
    plt.plotfile(faname, ('date','macdh','macd','macds'), plotfuncs={'macdh': 'bar'}, subplots=False)
    
    #plt.plotfile(faname, ('date','macdh'), newfig=False, plotfuncs={'macdh': 'bar'}, subplots=False)
    
    
    
    #[u' u'Solarize_Light2', u'seaborn-notebook', u'classic', u'seaborn-ticks', u'grayscale', u'bmh', u'seaborn-talk', u'dark_background', u'ggplot', u'fivethirtyeight', u'_classic_test', u'seaborn-colorblind', u'seaborn-deep', u'seaborn-whitegrid', u'seaborn-bright', u'seaborn-poster', u'seaborn-muted', u'seaborn-paper', u'seaborn-white', u'fast', u'seaborn-pastel', u'seaborn-dark', u'seaborn', u'seaborn-dark-palette']
    plt.savefig(line+'_macd.png')