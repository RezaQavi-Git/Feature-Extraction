import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

from utils import *
from utils.basic import create_dataframe
from utils.cross_value import cross_value_from_above, cross_value_from_bottom
from utils.difference_from_line import difference_from_line
from utils.sum_in_period import *

def ema(df):
    ema_value_5 = ta.ema(df['close'], length=5)
    ema_value_10 = ta.ema(df['close'], length=10)
    ema_value_20 = ta.ema(df['close'], length=20)
    ema_value_50 = ta.ema(df['close'], length=50)
    ema_value_100 = ta.ema(df['close'], length=100)

    diff_from_price = difference_from_line(ema_value_5, df['close'])
    cross_line_bullish_5_10 = cross_line_bullish(ema_value_5, ema_value_10)
    cross_line_bearish_5_10 = cross_line_bearish(ema_value_5, ema_value_10)

    cross_line_bullish_5_20 = cross_line_bullish(ema_value_5, ema_value_20)
    cross_line_bearish_5_20 = cross_line_bearish(ema_value_5, ema_value_20)

    cross_line_bullish_5_50 = cross_line_bullish(ema_value_5, ema_value_50)
    cross_line_bearish_5_50 = cross_line_bearish(ema_value_5, ema_value_50)

    cross_line_bullish_5_100 = cross_line_bullish(ema_value_5, ema_value_100)
    cross_line_bearish_5_100 = cross_line_bearish(ema_value_5, ema_value_100)

    # TODO 
    d = {
        'ema_value_5': ema_value_5,
        'ema_diff_from_price': diff_from_price,
        'ema_cross_line_bullish_5_10': cross_line_bullish_5_10,
        'ema_cross_line_bearish_5_10': cross_line_bearish_5_10,
        'ema_cross_line_bullish_5_20': cross_line_bullish_5_20,
        'ema_cross_line_bearish_5_20': cross_line_bearish_5_20,
        'ema_cross_line_bullish_5_50': cross_line_bullish_5_50,
        'ema_cross_line_bearish_5_50': cross_line_bearish_5_50,
        'ema_cross_line_bullish_5_100': cross_line_bullish_5_100,
        'ema_cross_line_bearish_5_100': cross_line_bearish_5_100,
    }

    return create_dataframe(d)