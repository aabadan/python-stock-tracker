# -*- coding: utf-8 -*-
"""
Created on Tue May 30 12:58:51 2017

@author: Alican
"""

from googlefinance import getQuotes
#import json


def getStockInfo(index,symbol):
    
    quoteStr = index + ':' + symbol
    data = getQuotes(quoteStr)
    result = []
    for d in data:
        result.append(d['StockSymbol'])
        result.append(d['Index'])
        result.append(d['LastTradeWithCurrency'])
        result.append(d['LastTradeDateTime'])
        result.append(d['LastTradeTime'])
    
    return result
    
