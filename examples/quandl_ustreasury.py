# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 22:35:51 2017

@author: syono
"""

from  pyeconfindata.interestrate import *
import pyeconfindata.source.quandl as quandlsource

source= quandlsource.QuandlSource("oPAL8s4KyTyVUjzz1SrR")

data = us_treasury_historical_quandl(source, "2016-01-01", "2016-01-10")
print(data.head())

data = us_treasury_historical_quandl(source, "2016-01-01", "2016-01-10", ['M01', 'M03'])
print(data.head())