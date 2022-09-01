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
    df.to_csv(file_name, sep=',')

def load_dataframe(name):
    data= pd.read_csv('data\export_{0}_5m.csv'.format(name))
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
    for c in coins:
        df = load_dataframe(c)

        features = create_features_dataframe(df)
        extracted_df = pd.concat([df, features], axis=1)

        write_to_file(extracted_df, '{0}.csv'.format(c))


if __name__ == "__main__":
    main()