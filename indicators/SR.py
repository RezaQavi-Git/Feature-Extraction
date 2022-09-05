import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

from utils.config import *

from utils import *
from utils.basic import create_dataframe
from utils.config import PERIOD
from utils.support_resistance import *


def in_levels(levels, j):
    for i in range(len(levels)):
        if(j == levels[i][0]):
            return True
    return False

def SR(df):
    nearest_support = [0] * len(df[CLOSE_COLUMN])
    nearest_resistance = [0] * len(df[CLOSE_COLUMN])
    point = [0] * len(df[CLOSE_COLUMN])

    levels = find_support_resistance_levels(df)
    for i in range(len(df[CLOSE_COLUMN])):
        nearest_support[i] = min_support(df[CLOSE_COLUMN][i], levels)
        nearest_resistance[i] = min_resistance(df[CLOSE_COLUMN][i], levels)
    
    for i in range(len(df[CLOSE_COLUMN])):
        if in_levels(levels, i):
            point[i] = 1
    

    d = {
        'SR_point': point,
        'SR_nearest_support': nearest_support,
        'SR_nearest_resistance': nearest_resistance,
    }

    return create_dataframe(d)