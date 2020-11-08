# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 14:46:24 2020

@author: Schre
"""

import sqlite3
import csv
from Path_Validation import symbol

#Sets Connection to our Stocks Database
connection = sqlite3.connect("Stocks.db")
cursor = connection.cursor()

#Opens csv file from users requested Stock Symbol, loads into Predetermined table --This will currently error out if the table does not exists in the DB
with open('{}.csv'.format(symbol),'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO {} values (?,?,?,?,?,?,?,?)".format(symbol), row.split(",") )
        connection.commit()
        no_records += 1
connection.close()
print("/n {} Records Transferred".format(no_records))
                      
