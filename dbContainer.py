# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 20:30:47 2017

@author: Alican
"""

import sqlite3

def insertStocksDB(data):

    conn = sqlite3.connect('mydb.sqlite')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS stocks')
    cur.execute('CREATE TABLE stocks (name TEXT, company TEXT, companyCode TEXT)')
    
    cur.executemany('INSERT INTO stocks (name, company, companyCode) VALUES (?,?,?)', data)
    conn.commit()
    conn.close()
    
def getStockListDB(stockMarketName):
    
    conn = sqlite3.connect('mydb.sqlite')
    cur = conn.execute('SELECT * from stocks where name=?',(stockMarketName,))
    stockList = cur.fetchall()
    conn.close()
    
    return stockList