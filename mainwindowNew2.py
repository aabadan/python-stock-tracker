# -*- coding: utf-8 -*-
"""
Created on Tue May 30 12:58:51 2017

@author: Alican
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from resultPage import Ui_Form
from collections import OrderedDict
from get_stock_list import getStockList
from dbContainer import insertStocksDB,getStockListDB
from googleFinance import getStockInfo

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 791, 471))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(290, 55, 181, 21))
        self.label.setObjectName("label")
        self.stockCombo = QtWidgets.QComboBox(self.page)
        self.stockCombo.setGeometry(QtCore.QRect(270, 140, 191, 31))
        self.stockCombo.setObjectName("stockCombo")
        ########################COMBO FILL#####################################
        self.items = OrderedDict([('Select Stock Market', ''),('IST', ''),
                                ('NYSE', ''),
                                ('NASDAQ', ''),
                                ])
        self.stockCombo.addItems(self.items.keys())
        #######################################################################
        self.loadButton = QtWidgets.QPushButton(self.page)
        self.loadButton.setGeometry(QtCore.QRect(320, 240, 91, 31))
        self.loadButton.setObjectName("loadButton")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.backButton = QtWidgets.QPushButton(self.page_2)
        self.backButton.setGeometry(QtCore.QRect(30, 430, 91, 31))
        self.backButton.setObjectName("backButton")
        self.shareInfoButton = QtWidgets.QPushButton(self.page_2)
        self.shareInfoButton.setGeometry(QtCore.QRect(680, 430, 91, 31))
        self.shareInfoButton.setObjectName("shareInfoButton")
        self.tableWidget = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget.setGeometry(QtCore.QRect(50, 40, 691, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.backButton2 = QtWidgets.QPushButton(self.page_3)
        self.backButton2.setGeometry(QtCore.QRect(30, 420, 91, 31))
        self.backButton2.setObjectName("backButton2")
        self.setAlarmButton = QtWidgets.QPushButton(self.page_3)
        self.setAlarmButton.setGeometry(QtCore.QRect(670, 420, 91, 31))
        self.setAlarmButton.setObjectName("setAlarmButton")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(50, 30, 691, 351))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #################################################################
        self.loadButton.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1))
        self.backButton.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(0))
        self.shareInfoButton.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(2))
        self.backButton2.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1))
        self.setAlarmButton.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(0))
        
        self.loadButton.clicked.connect(lambda :self.load_button_pressed())

        #########################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Stack Exchange Report Tool"))
        self.loadButton.setText(_translate("MainWindow", "Load"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.shareInfoButton.setText(_translate("MainWindow", "Get Share Info"))
        self.backButton2.setText(_translate("MainWindow", "Back"))
        self.setAlarmButton.setText(_translate("MainWindow", "Set Alarm"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Stock Market"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Company"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Share Code"))
        self.backButton2.setText(_translate("MainWindow", "Back"))
        self.setAlarmButton.setText(_translate("MainWindow", "Set Alarm"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "StockSymbol"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Index"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "LastTradeWithCurrency"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "LastTradeDateTime"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "LastTradeDateTime"))
        
    def load_button_pressed(self):
        stockSelection =  str(self.stockCombo.currentText())
        print('Load Button pressed for',stockSelection)
        stockList = getStockListDB(stockSelection)
        #print(len(stockList))
        if len(stockList) == 0:
            if stockSelection != "Select Stock Market":
                compList,symList = getStockList(stockSelection)
                
            compList,symList = getStockList(stockSelection)
            stockStr =[]
            for a in range(0,len(compList)):
                stockStr.append(stockSelection)
            
            data = zip(stockStr,compList,symList)
            #print(data)
            insertStocksDB(data)
            #######################
            print("Stocks saved to DB")
            ######################
            stockList = getStockListDB(stockSelection)
            #######################
            print("Stocks retrieved from DB")
            ######################
        self.setmydataOnPage(stockList)
        #print(stockList);
        
    def setmydataOnPage(self,data):
        print("setmydataOnPage")
        #print(len(data))
        self.tableWidget.setRowCount(len(data))
        for n, key in enumerate(data):
            for m, item in enumerate(key):
                newitem = QtWidgets.QTableWidgetItem(item)
                self.tableWidget.setItem(n, m, newitem)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.itemSelectionChanged.connect(self.print_row)
        
    def print_row(self):
        items = self.tableWidget.selectedItems()
        if len(items) == 3:
            print(str(items[2].text()) + " selected")
            try:
                result = getStockInfo(str(items[0].text()),str(items[2].text()))
                self.showSelection(result)
            except IndexError:
                self.shareInfoButton.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1))
        
    def showSelection(self,data):
        print("showSelection")
        for m, item in enumerate(data):
                newitem = QtWidgets.QTableWidgetItem(item)
                self.tableWidget_2.setItem(0, m, newitem)
        header = self.tableWidget_2.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

