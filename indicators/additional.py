import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

from utils import *
from utils.basic import create_dataframe
from utils.sum_in_period import *

def additional(df):
    obv_value = ta.obv(df['close'], df['volume'])
    rvi_value = ta.rvi(df['high'], df['low'], df['close'])

    # TODO 
    d = {
        'obv_value': obv_value,
        'rvi_value': rvi_value,
    }

    return create_dataframe(d)