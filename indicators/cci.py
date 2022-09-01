import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

from utils import *
from utils.basic import create_dataframe
from utils.cross_value import cross_value_from_above, cross_value_from_bottom
from utils.sum_in_period import *

def cci(df):
    cci_value = ta.cci(df['high'], df['low'], df['close'])

    cross_200_pos = cross_value_from_bottom(cci_value, value=200)
    cross_200_neg = cross_value_from_above(cci_value, value=-200)
    cross_100_pos = cross_value_from_bottom(cci_value, value=100)
    cross_100_neg = cross_value_from_above(cci_value, value=-100)
    cross_0_pos = cross_value_from_bottom(cci_value, value=0)
    cross_0_neg = cross_value_from_above(cci_value, value=0)

    positive_change_sum = sum_in_period_positive(cci_value, period=14)
    negative_change_sum = sum_in_period_negative(cci_value, period=14)
    # TODO 
    d = {
        'cci_value': cci_value,
        'cci_cross_200_pos': cross_200_pos,
        'cci_cross_200_neg': cross_200_neg,
        'cci_cross_100_pos': cross_100_pos,
        'cci_cross_100_neg': cross_100_neg,
        'cci_cross_0_pos': cross_0_pos,
        'cci_cross_0_neg': cross_0_neg,
        'cci_positive_change_sum': positive_change_sum,
        'cci_negative_change_sum': negative_change_sum
    }

    return create_dataframe(d)