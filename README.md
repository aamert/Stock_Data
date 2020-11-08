# Stock_Data
Using Yfinance, download all historical stock data of your choice.

When running the script, you will be prompted to input your stock symbol of choice. script will check if the corresponding csv exists and whether it has been updated today. if it has been the script will stop with no changes made. otherwise it will download the most recent data to csv from yfinance

goals for the project: 
1. Currently if an incorrect Stock symbol is entered, CSV file is created anyway - Need to Fix
2. Load into SqlLite
