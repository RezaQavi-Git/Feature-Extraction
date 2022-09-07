import pandas as pd
# import pandas_ta as ta
from ta.momentum import RSIIndicator, StochRSIIndicator, WilliamsRIndicator, AwesomeOscillatorIndicator

import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

from utils.config import *

from utils import *
from utils.basic import create_dataframe
from utils.cross_line import cross_line_bearish, cross_line_bullish, cross_line_from_above, cross_line_from_bottom
from utils.cross_value import cross_value_from_above, cross_value_from_bottom
from utils.sum_in_period import *

STOCH_K_DEFULT = 14
STOCH_D_DEFULT = 3

def stoch(df):
    stoch_value = StochRSIIndicator(df[CLOSE_COLUMN], fillna=True)
    K_cross_20_above = cross_value_from_above(stoch_value.stochrsi_k(), 20)
    K_cross_20_bottom = cross_value_from_bottom(stoch_value.stochrsi_k(), 20)
    K_cross_50_above = cross_value_from_above(stoch_value.stochrsi_k(), 50)
    K_cross_50_bottom = cross_value_from_bottom(stoch_value.stochrsi_k(), 50)
    K_cross_80_above = cross_value_from_above(stoch_value.stochrsi_k(), 80)
    K_cross_80_bottom = cross_value_from_bottom(stoch_value.stochrsi_k(), 80)

    D_cross_20_above = cross_value_from_above(stoch_value.stochrsi_d(), 20)
    D_cross_20_bottom = cross_value_from_bottom(stoch_value.stochrsi_d(), 20)
    D_cross_50_above = cross_value_from_above(stoch_value.stochrsi_d(), 50)
    D_cross_50_bottom = cross_value_from_bottom(stoch_value.stochrsi_d(), 50)
    D_cross_80_above = cross_value_from_above(stoch_value.stochrsi_d(), 80)
    D_cross_80_bottom = cross_value_from_bottom(stoch_value.stochrsi_d(), 80)

    K_cross_D_bullish = cross_line_bullish(stoch_value.stochrsi_k(), stoch_value.stochrsi_d())
    K_cross_D_bearish = cross_line_bearish(stoch_value.stochrsi_k(), stoch_value.stochrsi_d())


    d = {
        'stochrsi_value': stoch_value.stochrsi(),
        'stoch_K_value': stoch_value.stochrsi_k(),
        'stoch_D_value':stoch_value.stochrsi_d(),
        'stoch_K_cross_20_above':K_cross_20_above,
        'stoch_K_cross_20_bottom': K_cross_20_bottom,
        'stoch_K_cross_50_above':K_cross_50_above,
        'stoch_K_cross_50_bottom': K_cross_50_bottom,
        'stoch_K_cross_80_above':K_cross_80_above,
        'stoch_K_cross_80_bottom': K_cross_80_bottom,
        'stoch_D_cross_20_above':D_cross_20_above,
        'stoch_D_cross_20_bottom': D_cross_20_bottom,
        'stoch_D_cross_50_above':D_cross_50_above,
        'stoch_D_cross_50_bottom': D_cross_50_bottom,
        'stoch_D_cross_80_above':D_cross_80_above,
        'stoch_D_cross_80_bottom': D_cross_80_bottom,
        'stoch_K_cross_D_bullish': K_cross_D_bullish,
        'stoch_K_cross_D_bearish': K_cross_D_bearish,
    }

    return create_dataframe(d)
    