import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

from utils import *
from utils.basic import create_dataframe
from utils.cross_line import cross_line_bearish, cross_line_bullish
from utils.difference_from_line import difference_from_line
from utils.sum_in_period import *

def sma(df):
    sma_value_5 = ta.sma(df['close'], length=5)
    sma_value_10 = ta.sma(df['close'], length=10)
    sma_value_20 = ta.sma(df['close'], length=20)
    sma_value_50 = ta.sma(df['close'], length=50)
    sma_value_100 = ta.sma(df['close'], length=100)

    diff_from_price = difference_from_line(sma_value_5, df['close'])
    cross_line_bullish_5_10 = cross_line_bullish(sma_value_5, sma_value_10)
    cross_line_bearish_5_10 = cross_line_bearish(sma_value_5, sma_value_10)

    cross_line_bullish_5_20 = cross_line_bullish(sma_value_5, sma_value_20)
    cross_line_bearish_5_20 = cross_line_bearish(sma_value_5, sma_value_20)

    cross_line_bullish_5_50 = cross_line_bullish(sma_value_5, sma_value_50)
    cross_line_bearish_5_50 = cross_line_bearish(sma_value_5, sma_value_50)

    cross_line_bullish_5_100 = cross_line_bullish(sma_value_5, sma_value_100)
    cross_line_bearish_5_100 = cross_line_bearish(sma_value_5, sma_value_100)

    d = {
        'sma_value_5': sma_value_5,
        'sma_diff_from_price': diff_from_price,
        'sma_cross_line_bullish_5_10': cross_line_bullish_5_10,
        'sma_cross_line_bearish_5_10': cross_line_bearish_5_10,
        'sma_cross_line_bullish_5_20': cross_line_bullish_5_20,
        'sma_cross_line_bearish_5_20': cross_line_bearish_5_20,
        'sma_cross_line_bullish_5_50': cross_line_bullish_5_50,
        'sma_cross_line_bearish_5_50': cross_line_bearish_5_50,
        'sma_cross_line_bullish_5_100': cross_line_bullish_5_100,
        'sma_cross_line_bearish_5_100': cross_line_bearish_5_100,
    }

    return create_dataframe(d)