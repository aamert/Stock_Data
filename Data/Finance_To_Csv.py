# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 00:30:00 2020

@author: JTSC
"""

import pathlib
import os.path
import time
from datetime import date
import yfinance as yf

#Users Input for Stock Symbol
def Users_input():
    return input()

#Sets Users Input
symbol = Users_input()

#Sets Filepath For Current File
path = os.path.dirname(__file__)


#Returns the final requested stocks filepath
def Stock_Filepath():
    filepath = (path + "\{}.csv").format(symbol) 
    return str(filepath)

#Sets Stock Filepath with Attached CSV
filepath = Stock_Filepath()

  
#Checks if Stock File Exists
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
#Sets result answer to 1:0 based on Stock_exists( function)   
Stock_Existing_Test = Stock_exists()
    
#Used to download stock information    
def csv_download():
    #Gets Stock Symbol Information
    tickers = yf.Ticker(symbol)

    #Generates Max Range of Data
    hist = tickers.history(period="max").reset_index()
    #Causes an exception error: This is needed in order to not download csv files with no data due to invalid stock symbols E.G. (TSLA would be excepted, dushoqysh would not be)
    try:
        if hist.empty:
            print("Invalid Symbol - Please Try Again")
    except:
        print("data is empty")
        raise Exception
    else:
        return hist

    #Creates a CSV filename Based on User Input
    fileName = "{}.csv".format(symbol)

    #Uses Filename to Create CSV File
    hist.to_csv(fileName,
            index=False,
            sep=",")
    return print("Downloaded")
    

    #Checks to see if Stock Symbol CSV Exists
def file_check():        
    #stock_exists checks if file exists - if it does, Checks if file was updated today.
    if Stock_Existing_Test == 1:
        print("File Up To Date")
        
    #If Stock doesn't exists, it gets downloaded
    else:
        csv_download()


#Set for file initialization in spyder
file_check() 
