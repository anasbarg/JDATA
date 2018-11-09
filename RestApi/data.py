import numpy as np
import pandas as pd


def smoothexp(y, a):
    z = np.zeros(y.shape[0])  # zero initialisation
    z = pd.Series(z)  # converting to a panda series
    for i in range(y.shape[0]-2):
        z[i+1] = y.iloc[i+1]*a+(1-a)*z[i]  # EWMA smoothing
    z = z/np.sum(z)  # Normalization step
    return z


def distribution(year, a, path):
    df = pd.read_csv(path)  # a dataframe that forms the main source of data
    # a filtered dataframe that only contains data for the year of interest
    df_year = df[df.year == year]
    # the x-axis is log scale of the average monthly income in the year of interest
    x = np.log10(df_year.AverageIncome/12)
    y = df_year.pdf  # the exact distribution function in that year
    z = smoothexp(y, a)  # is the smoothed distribution function at that year
    return (round(x, 2), y, z)


def share(p_start, p_end, Year_from, Year_to, path):
    df = pd.read_csv(path)  # a dataframe that forms the main source of data
    df_share1 = df[(df.year >= Year_from) & (df.year <= Year_to) & (df.start >= p_start) & (
        df.start < p_end)].copy()  # filter required population and time period
    df_share1 = df_share1.groupby('year').sum()  # calculate share
    return df_share1[['Share']]*100


def Threshold_range(p_start, p_end, Year_from, Year_to, path):
    df = pd.read_csv(path)  # a dataframe that forms the main source of data
    df_threshold1 = df[(df.year >= Year_from) & (df.year <= Year_to) & (df.start >= p_start) & (
        df.start <= p_end)].copy()  # filter required population and time period
    df_threshold1 = df_threshold1.groupby('year')  # calculate share
    aggregation = {
        'Threshold(JOD)': {'threshold_min': 'min', 'threshold_max': 'max'}}
    return df_threshold1.agg(aggregation)


def AverageIncome(p_start, p_end, Year_from, Year_to, path):
    df = pd.read_csv(path)  # a dataframe that forms the main source of data
    df_Average1 = df[(df.year >= Year_from) & (df.year <= Year_to) & (df.start >= p_start) & (
        df.start <= p_end)].copy()  # filter required population and time period
    df_Average1 = df_Average1.groupby('year')  # calculate share
    aggregation = {'AverageIncome': {
        'Average_min': 'min', 'Average_max': 'max'}}
    return df_Average1.agg(aggregation)
