import yfinance as yf

# Load Nifty 50 data from Yahoo Finance
nifty50 = yf.download('^NSEI', start='2019-01-01', end='2022-02-22')

# Print the first five rows of the data
print(nifty50.head())

import matplotlib.pyplot as plt

# Plot the Nifty 50 index
plt.figure(figsize=(12,6))
plt.plot(nifty50['Close'])
plt.title('Nifty 50 Index')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

# Calculate daily returns
nifty50['Returns'] = nifty50['Close'].pct_change()

# Plot the daily returns
plt.figure(figsize=(12,6))
plt.plot(nifty50['Returns'])
plt.title('Nifty 50 Daily Returns')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.show()

import numpy as np

# Calculate annualized volatility
volatility = np.sqrt(252) * nifty50['Returns'].std()

print("Annualized Volatility:", round(volatility*100, 2), "%")

# Calculate 50-day rolling mean and standard deviation
nifty50['Rolling Mean'] = nifty50['Close'].rolling(window=50).mean()
nifty50['Rolling Std'] = nifty50['Close'].rolling(window=50).std()

# Plot rolling mean and standard deviation
plt.figure(figsize=(12,6))
plt.plot(nifty50['Close'], label='Nifty 50 Index')
plt.plot(nifty50['Rolling Mean'], label='Rolling Mean')
plt.plot(nifty50['Rolling Std'], label='Rolling Std')
plt.legend()
plt.title('Nifty 50 Index with Rolling Statistics')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
