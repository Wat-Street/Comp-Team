import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pairs = ['dot-usdt', 'ltc-usdt', 'trx-usdt']
for pair in pairs:
  # Read in data
  df_binance = pd.read_csv(f'data/binance/{pair}.csv')
  df_binance['time'] = pd.to_datetime(df_binance['time'], unit='ms')
  df_poloniex = pd.read_csv(f'data/poloniex/{pair}.csv')
  df_poloniex['time'] = pd.to_datetime(df_poloniex['time'], unit='ms')

  # Plot data
  plt.plot(df_binance['time'], df_binance['price'], label='Binance')
  plt.plot(df_poloniex['time'], df_poloniex['price'], label='Poloniex')
  plt.xlabel('Time')
  plt.ylabel('Price')
  plt.title(f'{pair} Price')
  plt.legend()
  plt.show()
