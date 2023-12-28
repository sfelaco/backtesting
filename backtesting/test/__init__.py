"""Data and utilities for testing."""
import pandas as pd


def _read_file(filename):
    from os.path import dirname, join

    return pd.read_csv(join(dirname(__file__), filename),
                       index_col=0, parse_dates=True, infer_datetime_format=True)


GOOG = _read_file('GOOG.csv')
"""DataFrame of daily NASDAQ:GOOG (Google/Alphabet) stock price data from 2004 to 2013."""

EURUSD = _read_file('EURUSD.csv')
"""DataFrame of hourly EUR/USD forex data from April 2017 to February 2018."""

DE40_2D_5M =  _read_file('DE40_2d_5m.csv')
"""DataFrame of 5M DE40 index data from 19 Dec 2023 to 20 Dec 2023."""

DE40_5Y_5M =  _read_file('DE40_5y_5m.csv')
"""DataFrame of 5M DE40 index data from 20 Dec 2022 to 20 Dec 2023."""

DE40_5M_5M =  _read_file('DE40_1M_5m.csv')
"""DataFrame of 5M DE40 index data from 20 Nov 2023 to 20 Dec 2023."""

def SMA(arr: pd.Series, n: int) -> pd.Series:
    """
    Returns `n`-period simple moving average of array `arr`.
    """
    return pd.Series(arr).rolling(n).mean()
