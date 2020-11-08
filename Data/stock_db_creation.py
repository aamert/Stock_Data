import sqlite3

#Setting SQL Lite DB Connection File
conn = sqlite3.connect('Stocks.db')
print ("Opened database successfully")

#Creates requested table with fields matching what's provided in previous csv files from Path_Validation
conn.execute('''CREATE TABLE TSLA
         (Date date PRIMARY KEY     NOT NULL,
         Open          Decimal(10,2),    
         High          Decimal(10,2),     
         Low           Decimal(10,2),
         Close         Decimal(10,2),
         Volume        INT,
         Dividends     INT,
         [Stock Splits] Decimal(3,2));''')
print ("Table created successfully")

conn.close()