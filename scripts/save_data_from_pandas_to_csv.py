#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 18:58:05 2018
@author: linux
"""
import pandas_datareader.data as web
from datetime import datetime
import os, sys
from pandas_datareader._utils import RemoteDataError

file_path = "csv_files"

os.mkdir( file_path, 0755 );

from_date = os.environ['FROM_DATE']
to_date = os.environ['TO_DATE']

with open('all_symbols.txt') as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        for line in content:
            try:
                data1 = web.DataReader(line, 'iex', from_date, to_date)
            except RemoteDataError:
                continue
            data1.to_csv('csv_files/'+line+'.csv')
