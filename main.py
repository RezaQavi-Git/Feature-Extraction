import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
from indicators.bb import bb
from indicators.ema import ema

from indicators.ichimoku import ichimoku
from indicators.mfi import mfi
from indicators.rsi import rsi


data= pd.read_csv("data\export_BTCUSDT_5m.csv")
df = pd.DataFrame(data)

# rsi_df = rsi(df)
# mfi_df = mfi(df)
# ichimoku_df = ichimoku(df)
ema_df = ema(df)
ema_df = ema_df.fillna(0)
print(ema_df)
# print(ichimoku_df['ichimoku_diff_tenkan_with_kijun'][:50])
# print(ichimoku_df['ichimoku_tenkan_sen'][:25])
# print(ichimoku_df['ichimoku_kijun_sen'][:30])
# print(mfi_df['mfi_crossed_20'].value_counts())

# print(df.ta.indicators())

# print(help(ta.ema))
# print(ta.ema(df['close'], length=10))
