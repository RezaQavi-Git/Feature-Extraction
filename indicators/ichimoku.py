import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
 
from utils.basic import create_dataframe
from utils.difference_from_line import difference_from_line
from utils.sum_in_period import *

def ichimoku(df):
    ichimoku_value = ta.ichimoku(df['high'], df['low'], df['close'])
    diff_tenkan_sen_with_close = difference_from_line(ichimoku_value[0]['ITS_9'], df['close'])
    diff_kijun_sen_with_close = difference_from_line(ichimoku_value[0]['IKS_26'], df['close'])
    diff_span_A_with_close = difference_from_line(ichimoku_value[0]['ISA_9'], df['close'])
    diff_span_B_with_close = difference_from_line(ichimoku_value[0]['ISB_26'], df['close'])
    diff_span_A_with_span_B = difference_from_line(ichimoku_value[0]['ISA_9'], ichimoku_value[0]['ISB_26'])
    diff_tenkan_with_kijun = difference_from_line(ichimoku_value[0]['ITS_9'], ichimoku_value[0]['IKS_26'])

    # TODO
    d = {
        'ichimoku_span_A': ichimoku_value[0]['ISA_9'],
        'ichimoku_span_B':  ichimoku_value[0]['ISB_26'],
        'ichimoku_tenkan_sen':  ichimoku_value[0]['ITS_9'],
        'ichimoku_kijun_sen':  ichimoku_value[0]['IKS_26'],
        'ichimoku_diff_span_A_with_close':  diff_span_A_with_close,
        'ichimoku_diff_span_B_with_close':  diff_span_B_with_close,
        'ichimoku_diff_tenkan_sen_with_close':  diff_tenkan_sen_with_close,
        'ichimoku_diff_kijun_sen_with_close':  diff_kijun_sen_with_close,
        'ichimoku_diff_span_A_with_span_B':  diff_span_A_with_span_B,
        'ichimoku_diff_tenkan_with_kijun':  diff_tenkan_with_kijun
    }

    return create_dataframe(d)