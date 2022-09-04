import os
from pyexpat import features
import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

from indicators.additional import additional
from indicators.adx import adx
from indicators.aroon import aroon
from indicators.bb import bb
from indicators.cci import cci
from indicators.ema import ema

from indicators.ichimoku import ichimoku
from indicators.macd import macd
from indicators.mfi import mfi
from indicators.rsi import rsi
from indicators.sma import sma
from indicators.stoch import stoch
from indicators.trend import trend
from indicators.wr import wr
from utils.config import DURATION, EXPORTS_FOLDER, FILE_PATH, WRITE_FILE_PATH



coins = [
    'BTCUSDT',
    'ETHUSDT',
    'ADAUSDT'
]

functions = [
    additional,
    adx,
    aroon,
    bb,
    cci,
    ema,
    ichimoku,
    macd,
    mfi,
    rsi,
    sma,
    stoch,
    wr,
    trend
]

def fill_nan(df):
    return df.fillna(0)


def write_to_file(df, file_name):
    if not os.path.exists(EXPORTS_FOLDER):
        os.mkdir(EXPORTS_FOLDER)
    fullname = os.path.join(EXPORTS_FOLDER, file_name)   
    df.to_csv(fullname, sep=',')

def load_dataframe(name):
    data= pd.read_csv(FILE_PATH.format(name, DURATION))
    df = pd.DataFrame(data)

    return df

def create_features_dataframe(df):
    features_df = pd.DataFrame()
    df_list = []

    for i in range(len(functions)):
        df_ = fill_nan(functions[i](df))
        df_list.append(df_)

    features_df = pd.concat(df_list, axis=1)

    return features_df


def main():
    print('Start extrarting features : ...')
    for c in coins:
        print('\t Strat {0} feature extraction . . . '.format(c))
        df = load_dataframe(c)

        features = create_features_dataframe(df)
        extracted_df = pd.concat([df, features], axis=1)

        write_to_file(extracted_df, WRITE_FILE_PATH.format(c))
        print('\t Stop {0} feature extraction.You can find result in this path : {1}'.format(c, WRITE_FILE_PATH.format(c)))

    print('\t End of extraction. enjoy :)')


if __name__ == "__main__":
    main()