import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
from utils.config import *
from ta.trend import SMAIndicator, EMAIndicator, MACD, ADXIndicator, IchimokuIndicator, CCIIndicator, AroonIndicator
 
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
    ichimoku_value = IchimokuIndicator(df[HIGH_COLUMN], df[LOW_COLUMN], fillna=True)
    
    diff_tenkan_sen_with_close = difference_from_line(ichimoku_value.ichimoku_conversion_line(), df[CLOSE_COLUMN])
    diff_kijun_sen_with_close = difference_from_line(ichimoku_value.ichimoku_base_line(), df[CLOSE_COLUMN])
    diff_span_A_with_close = difference_from_line(ichimoku_value.ichimoku_a(), df[CLOSE_COLUMN])
    diff_span_B_with_close = difference_from_line(ichimoku_value.ichimoku_b(), df[CLOSE_COLUMN])
    diff_span_A_with_span_B = difference_from_line(ichimoku_value.ichimoku_a(), ichimoku_value.ichimoku_b())
    diff_tenkan_with_kijun = difference_from_line(ichimoku_value.ichimoku_conversion_line(), ichimoku_value.ichimoku_base_line())

    tenkan_cross_kijun = cross_line_from_above(ichimoku_value.ichimoku_conversion_line(), ichimoku_value.ichimoku_base_line())
    kijun_cross_tenkan = cross_line_from_bottom(ichimoku_value.ichimoku_base_line(), ichimoku_value.ichimoku_conversion_line())

    cloud_color = cloud_color_detection(df[CLOSE_COLUMN], ichimoku_value.ichimoku_a(), ichimoku_value.ichimoku_b())
    d = {
        'ichimoku_span_A': ichimoku_value.ichimoku_a(),
        'ichimoku_span_B':  ichimoku_value.ichimoku_b(),
        'ichimoku_tenkan_sen':  ichimoku_value.ichimoku_conversion_line(),
        'ichimoku_kijun_sen':  ichimoku_value.ichimoku_base_line(),
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