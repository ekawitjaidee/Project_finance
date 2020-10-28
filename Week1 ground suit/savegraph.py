import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime
# from mpl_finance import candlestick_ohlc

start = datetime.datetime(2010,1,1)
end = datetime.datetime(2011,1,1)
df = web.DataReader('AAPL','yahoo',start,end)
df = df.drop(['Open','High','Low','Volume','Adj Close'],axis=1)
pd.set_option('display.max_columns', None)

df.loc['2010-02-18','signal'] = 'buy'
df.loc['2010-02-19','signal'] = 'buy'
df.loc['2010-02-22','signal'] = 'buy'
df.loc['2010-02-23','signal'] = 'buy'
df.loc['2010-02-24','signal'] = 'buy'#

df.loc['2010-03-12','signal'] = 'sold'#
df.loc['2010-03-15','signal'] = 'sold'
df.loc['2010-03-16','signal'] = 'sold'

df.loc['2010-03-19','signal'] = 'buy'#
df.loc['2010-03-22','signal'] = 'buy'
df.loc['2010-03-23','signal'] = 'buy'

df.loc['2010-04-26','signal'] = 'sold'#
df.loc['2010-04-27','signal'] = 'sold'
df.loc['2010-04-28','signal'] = 'sold'
df.loc['2010-04-29','signal'] = 'sold'

df.loc['2010-05-07','signal'] = 'buy' #
df.loc['2010-05-11','signal'] = 'buy'

df.loc['2010-05-14','signal'] = 'sold'
df.loc['2010-05-17','signal'] = 'sold' #
df.loc['2010-05-18','signal'] = 'sold'

df.loc['2010-05-20','signal'] = 'buy'
df.loc['2010-05-21','signal'] = 'buy' #
df.loc['2010-05-25','signal'] = 'buy'

df.loc['2010-06-01','signal'] = 'sold'
df.loc['2010-06-02','signal'] = 'sold' #
df.loc['2010-06-03','signal'] = 'sold'

df.loc['2010-06-08','signal'] = 'buy'#
df.loc['2010-06-09','signal'] = 'buy'
df.loc['2010-06-10','signal'] = 'buy'


df.loc['2010-06-17','signal'] = 'sold'#
df.loc['2010-06-18','signal'] = 'sold'
df.loc['2010-06-21','signal'] = 'sold'

df.loc['2010-07-01','signal'] = 'buy'
df.loc['2010-07-02','signal'] = 'buy'#
df.loc['2010-07-06','signal'] = 'buy'

df.loc['2010-07-08','signal'] = 'sold'
df.loc['2010-07-09','signal'] = 'sold'
df.loc['2010-07-12','signal'] = 'sold'#
df.loc['2010-07-13','signal'] = 'sold'#


df.loc['2010-07-15','signal'] = 'buy'
df.loc['2010-07-16','signal'] = 'buy' #
df.loc['2010-07-19','signal'] = 'buy'
df.loc['2010-07-20','signal'] = 'buy'
df.loc['2010-07-21','signal'] = 'buy'

df.loc['2010-08-02','signal'] = 'sold'
df.loc['2010-08-03','signal'] = 'sold' #
df.loc['2010-08-04','signal'] = 'sold'
df.loc['2010-08-05','signal'] = 'sold'
df.loc['2010-08-06','signal'] = 'sold'

df.loc['2010-08-25','signal'] = 'buy'
df.loc['2010-08-26','signal'] = 'buy'#
df.loc['2010-08-27','signal'] = 'buy'
df.loc['2010-08-30','signal'] = 'buy'#
df.loc['2010-08-31','signal'] = 'buy'

df.loc['2010-12-23','signal'] = 'sold'
df.loc['2010-12-27','signal'] = 'sold'
df.loc['2010-12-28','signal'] = 'sold'
df.loc['2010-12-29','signal'] = 'sold'
df.loc['2010-12-30','signal'] = 'sold'
df.loc['2010-12-31','signal'] = 'sold'

df['signal'] = np.where(df['signal'].isnull() ,'Wait or Hold',df['signal'])
df['buy'] = np.where(df['signal'] == 'buy',df['Close'],np.nan)
df['sold'] = np.where(df['signal'] == 'sold',df['Close'],np.nan)

plt.figure(figsize=(10,8))
plt.grid()
plt.title('Buy and Sold Signal')
plt.plot(df['Close'])
plt.plot(df['buy'],color='lightgreen')
plt.plot(df['sold'],color='red')
plt.ylabel('Price')
plt.xlabel('Date')
plt.show()