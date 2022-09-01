import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

from utils import *
from utils.basic import create_dataframe
from utils.cross_value import cross_value_from_above, cross_value_from_bottom
from utils.trending import trend_down, trend_up

def count_above_candle(l, period, value):
    counts = [0] * len(l)
    for i in range(period, len(l)):
        count = 0
        for j in range(i-period, i):
            if l[j] > value:
                count += 1
        counts[i] = count

    return counts

def count_bellow_candle(l, period, value):
    counts = [0] * len(l)
    for i in range(period, len(l)):
        count = 0
        for j in range(i-period, i):
            if l[j] < value:
                count += 1
        counts[i] = count

    return counts

def rsi(df):
    rsi_value = ta.rsi(df['close'])

    cross_70 = cross_value_from_bottom(rsi_value, value=70)
    cross_30 = cross_value_from_above(rsi_value, value=30)

    num_of_candle_above_70 = count_above_candle(rsi_value, period=14, value=70)
    num_of_candle_bellow_30 = count_bellow_candle(rsi_value, period=14, value=30)

    trending_up = trend_up(rsi_value, period=14)
    trending_down = trend_down(rsi_value, period=14)
    d = {
        'rsi_value': rsi_value,
        'rsi_crossed_70': cross_70,
        'rsi_crossed_30': cross_30,
        'rsi_num_of_candle_above_70': num_of_candle_above_70,
        'rsi_num_of_candle_bellow_30': num_of_candle_bellow_30,
        'rsi_trending_up': trending_up,
        'rsi_trending_down': trending_down
    }

    return create_dataframe(d)