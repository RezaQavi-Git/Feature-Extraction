import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

from utils import *
from utils.basic import create_dataframe
from utils.cross_value import cross_value_from_above, cross_value_from_bottom
from utils.sum_in_period import *

def mfi(df):
    mfi_value = ta.mfi(df['high'], df['low'], df['close'], df['volume'], fillna= True)

    cross_80 = cross_value_from_bottom(mfi_value, value=80)
    cross_20 = cross_value_from_above(mfi_value, value=20)

    positive_change_sum = sum_in_period_positive(mfi_value, period=14)
    negative_change_sum = sum_in_period_negative(mfi_value, period=14)
    # TODO 
    d = {
        'mfi_value': mfi_value,
        'mfi_crossed_80': cross_80,
        'mfi_crossed_20': cross_20,
        'mfi_positive_change_sum': positive_change_sum,
        'mfi_negative_change_sum': negative_change_sum
    }

    return create_dataframe(d)