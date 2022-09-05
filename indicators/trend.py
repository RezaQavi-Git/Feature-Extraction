import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

from utils.config import *

from utils import *
from utils.basic import create_dataframe
from utils.cross_value import cross_value_from_above, cross_value_from_bottom
from utils.sum_in_period import *
from utils.trending import trend_down, trend_neutral, trend_up

SHORT = 5
MID = 14
LONG = 28

def trend(df):

    short_trend_up = trend_up(df[CLOSE_COLUMN], period=SHORT)
    mid_trend_up = trend_up(df[CLOSE_COLUMN], period=MID)
    long_trend_up = trend_up(df[CLOSE_COLUMN], period=LONG)

    short_trend_down = trend_down(df[CLOSE_COLUMN], period=SHORT)
    mid_trend_down = trend_down(df[CLOSE_COLUMN], period=MID)
    long_trend_down = trend_down(df[CLOSE_COLUMN], period=LONG)

    short_trend_neutral = trend_neutral(short_trend_up, short_trend_down)
    mid_trend_neutral = trend_neutral(mid_trend_up, mid_trend_down)
    long_trend_neutral = trend_neutral(long_trend_up, long_trend_down)
    d = {
        'trend_short_trend_up': short_trend_up,
        'trend_mid_trend_up': mid_trend_up,
        'trend_long_trend_up': long_trend_up,
        'trend_short_trend_down': short_trend_down,
        'trend_mid_trend_down': mid_trend_down,
        'trend_long_trend_down': long_trend_down,
        'trend_short_trend_neutral': short_trend_neutral,
        'trend_mid_trend_neutral': mid_trend_neutral,
        'trend_long_trend_neutral': long_trend_neutral,
    }

    return create_dataframe(d)