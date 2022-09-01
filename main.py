import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

from indicators.mfi import mfi
from indicators.rsi import rsi


data= pd.read_csv("data\export_BTCUSDT_5m.csv")
df = pd.DataFrame(data)

# rsi_df = rsi(df)
# mfi_df = mfi(df)
mfi_df = mfi(df)

# print(mfi_df['mfi_crossed_80'].value_counts())
# print(mfi_df['mfi_crossed_20'].value_counts())