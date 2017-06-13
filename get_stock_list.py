# -*- coding: utf-8 -*-
"""
Created on Tue May 30 14:26:00 2017

@author: Alican
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import Label
import tkinter as tk

def getStockList(stockName):
    #https://www.google.com/finance?q=[(exchange%20%3D%3D%20%22NASDAQ%22)]&restype=company&noIL=1&num=30000
    urlPart1 = 'https://www.google.com/finance?q=[(exchange%20%3D%3D%20%22'
    exchange = stockName#'NASDAQ'
    urlPart2 = '%22)]&restype=company&noIL=1&num=30000'
    url =  urlPart1 + exchange + urlPart2

    html = urlopen(url)
    
    soup = BeautifulSoup(html,"html5lib")
    try:
        aTagsCom = [aTagCom.getText().strip() for aTagCom in soup.findAll('table', class_ = "gf-table company_results")[0].findAll('td', class_ = "localName nwp")]
        aTagsSym = [aTagSym.getText().strip() for aTagSym in soup.findAll('table', class_ = "gf-table company_results")[0].findAll('td', class_ = "symbol")]
    except IndexError:
        print('List finished')
            
    #print(len(aTagsCom))
    #print(len(aTagsSym))
    
    return aTagsCom,aTagsSym


'''
root = Tk()
hello = Label(master = root,
        width = 300,
        height = 200,
        borderwidth = 2,
        foreground = 'black',
        background = 'yellow',
        text = 'Stock Tracker')
aTagsCom,aTagsSym = getStockList('IST')
label = Label(root, text="\n".join(map(str, aTagsCom)))
label.pack()
hello.pack()
root.mainloop()
'''


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()
    #def getLists(self):
     #   aTagsCom,aTagsSym = getStockList('IST')
     #   return (aTagsCom, aTagsSym)

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 1")
       label.pack(side="top", fill="both", expand=True)
      
class Pages(Page):
    def __init__(self, *args, **kwargs):
        compList,symList = getStockList('IST')
        print(len(compList))
        print(len(symList))
        for i in range(0,len(compList),20):
            Page.__init__(self, *args, **kwargs)
            label = tk.Label(self, text=i)
            label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        #aTagsCom,aTagsSym = getStockList('IST')
        tk.Frame.__init__(self, *args, **kwargs)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        
        p1 = Page1(self)
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        b1 = tk.Button(buttonframe, text="1", command=p1.lift)
        b1.pack(side="left")
        
        #for i in range(0,len(Pages.compList),20):
        '''
        pNext = Pages(self)
        pNext.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        bNext = tk.Button(buttonframe, text="2", command=pNext.lift)
        bNext.pack(side="left")
        '''
        
        compList,symList = getStockList('IST')
        print(len(compList))
        print(len(symList))
        compStr = []
        for a in range(0,len(compList)):
            compStr.append('IST')
        print(len(compStr))
        for i in range(0,len(compList),20):
            Page.__init__(self, *args, **kwargs)
            
            newList = zip(compList,symList,compStr)
            #data = zip(newList,compStr)
            label = tk.Label(self, text="\n".join(map(str, newList)))
            label.pack(side="top", fill="both", expand=True)


        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
