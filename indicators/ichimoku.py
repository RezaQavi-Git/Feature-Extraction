import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
 
from utils.basic import create_dataframe
from utils.cross_line import cross_line_from_above, cross_line_from_bottom
from utils.difference_from_line import difference_from_line
from utils.sum_in_period import *


def cloud_color_detection(close, span_A, span_B):
    color = [0] * len(close)
    for i in range(len(close)):
        if ((span_A[i] > span_B[i]) and (close[i] < span_A[i]) and (close[i] > span_B[i]) ):
            color[i] = 1
        elif((span_B[i] > span_A[i]) and (close[i] < span_B[i]) and (close[i] > span_A[i]) ):
            color[i] = -1

    return color

def ichimoku(df):
    ichimoku_value = ta.ichimoku(df['high'], df['low'], df['close'])
    diff_tenkan_sen_with_close = difference_from_line(ichimoku_value[0]['ITS_9'], df['close'])
    diff_kijun_sen_with_close = difference_from_line(ichimoku_value[0]['IKS_26'], df['close'])
    diff_span_A_with_close = difference_from_line(ichimoku_value[0]['ISA_9'], df['close'])
    diff_span_B_with_close = difference_from_line(ichimoku_value[0]['ISB_26'], df['close'])
    diff_span_A_with_span_B = difference_from_line(ichimoku_value[0]['ISA_9'], ichimoku_value[0]['ISB_26'])
    diff_tenkan_with_kijun = difference_from_line(ichimoku_value[0]['ITS_9'], ichimoku_value[0]['IKS_26'])

    tenkan_cross_kijun = cross_line_from_above(ichimoku_value[0]['ITS_9'], ichimoku_value[0]['IKS_26'])
    kijun_cross_tenkan = cross_line_from_bottom(ichimoku_value[0]['IKS_26'], ichimoku_value[0]['ITS_9'])

    cloud_color = cloud_color_detection(df['close'], ichimoku_value[0]['ISA_9'], ichimoku_value[0]['ISB_26'])
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
        'ichimoku_diff_tenkan_with_kijun':  diff_tenkan_with_kijun,
        'ichimoku_tenkan_cross_kijun':  tenkan_cross_kijun,
        'ichimoku_kijun_cross_tenkan':  kijun_cross_tenkan,
        'ichimoku_price_in_cloud_color':  cloud_color,
    }

    return create_dataframe(d)