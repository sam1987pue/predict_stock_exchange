#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 23:58:02 2018

@author: linux
"""

import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import datetime as dt


def MACD(stock, start, end):
    df = web.DataReader('LQDT', 'iex', start, end) ['close']
    df = df.reset_index()
    df['30 mavg'] = pd.rolling_mean(df['close'], 30)
    df['26 ema'] = pd.ewma(df['close'], span=26)
    df['12 ema'] = pd.ewma(df['close'], span=12)
    df['MACD'] = (df['12 ema'] - df['26 ema'])
    df['Signal'] = pd.ewma(df['MACD'], span=9)
    df['Crossover'] = df['MACD'] - df['Signal']
    return stock, df['date'][-1:].to_string(),df['Crossover'][-1:].mean()
    

stocks = ['FB', 'AAPL', 'GOOG', 'AMZN', 'TSLA']

d = []

for stock in stocks:
    stock, date, macd = MACD(stock, '1/1/2016', dt.datetime.today())
    d.append({'Stock':stock, 'date':date, 'MACD':macd})
    
df2 = pd.DataFrame(d)
df2[['date', 'Stock', 'MACD']]

print df2