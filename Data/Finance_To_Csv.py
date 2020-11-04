# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:31:15 2020

@author: JTSC
"""
#Imports
import yfinance as yf
#import pandas as pd
#import sqlite3
#import csv
#import plotly_express as px

    #User Provided Stock Symbol
userInput = input().upper()

    #Gets Stock Symbol Information
tickers = yf.Ticker(userInput)

    #Generates Max Range of Data
hist = tickers.history(period="max").reset_index()

    #Creates a CSV filename Based on User Input
fileName = "{}.csv".format(userInput)

    #Uses Filename to Create CSV File
hist.to_csv(fileName,
            index=False,
            sep=",")
