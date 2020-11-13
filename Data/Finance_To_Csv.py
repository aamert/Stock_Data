# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12th 10:32:00.00.00

@author: JTSC
"""

import pathlib
import os.path
import time
from datetime import date
import yfinance as yf

path = os.path.dirname(__file__)
#############################################################
#Users Input for Stock Symbol
#############################################################
def Users_input():
    symbol = input()
    return symbol

#############################################################
#Sets Users Input
symbol = Users_input().upper()
#############################################################

#############################################################
#Sets Filepath For inputted csv
filepath = (path + "\{}.csv").format(symbol)
#############################################################

#############################################################
#Checks if Stock File Exists
#############################################################
def Stock_exists(): 
    #Checking to see if filepath Exists
    if pathlib.Path(filepath).exists() == True:
        
        #If Filepath Exists Check Last Date File Was updated, If today return 1 else 0
        if time.strftime('%Y-%m-%d', time.localtime(os.path.getmtime(filepath))) == str(date.today()):
            return 1
        else:
            return 0
    else:
        return 0
#############################################################
#Tries Inputted stock symbol to see if it's a valid symbol
#############################################################
def Try_Symbol():
    #Takes inputed symbol and checks if it's valid
     tickers = yf.Ticker(symbol)
     try:
        hist = tickers.history(period="max").reset_index()
        #If Hist is an empty dataframe, Raises error otherwise if valid and doesn't already exists, gets downloaded
        if hist.empty == True:
           raise 
        else:
                pass
     except:
        print("Try Again - Enter Valid Symbol")
     else:
         if Stock_exists() == 0:
        #1 means successful attempt at symbol set
             hist.to_csv(filepath,
            index=False,
            sep=",") ,print("downloaded") 
         else: 
             pass
#############################################################
    #Checks to see if Stock Symbol CSV Exists
#############################################################
def file_check():        
    if Stock_exists() == 1:
        return print(("{}.csv".format(symbol)))
    #If Stock doesn't exists, it gets downloaded
    else:
       return Try_Symbol()
 
file_check()
