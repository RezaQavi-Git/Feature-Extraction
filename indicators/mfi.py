import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

from utils import *
from utils.basic import create_dataframe
from utils.cross_value import cross_value_from_above, cross_value_from_bottom
from utils.sum_in_period import *
from utils.trending import trend_down, trend_up

def mfi(df):
    mfi_value = ta.mfi(df['high'], df['low'], df['close'], df['volume'])

    cross_80 = cross_value_from_bottom(mfi_value, value=80)
    cross_20 = cross_value_from_above(mfi_value, value=20)

    positive_change_sum = sum_in_period_positive(mfi_value, period=14)
    negative_change_sum = sum_in_period_negative(mfi_value, period=14)
    
    trending_up = trend_up(mfi_value, period=14)
    trending_down = trend_down(mfi_value, period=14)
    d = {
        'mfi_value': mfi_value,
        'mfi_crossed_80': cross_80,
        'mfi_crossed_20': cross_20,
        'mfi_positive_change_sum': positive_change_sum,
        'mfi_negative_change_sum': negative_change_sum,
        'mfi_trending_up': trending_up,
        'mfi_trending_down': trending_down
    }

    return create_dataframe(d)