__version__='1.0.2'
__author__ ='Matan Carmon'
__date__ = 'October 2023'


import pandas as pd
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri

# Activate automatic conversion of pandas objects to R objects
pandas2ri.activate()

# Install and import necessary R packages
# Make sure to install these packages in your R environment before running this code
# Example: install.packages(c("season", "seas", "timsac", "x13binary", "trend"))
robjects.r('''
    if (!requireNamespace("season", quietly = TRUE)) {
        install.packages("season")
    }
    if (!requireNamespace("seas", quietly = TRUE)) {
        install.packages("seas")
    }
    if (!requireNamespace("timsac", quietly = TRUE)) {
        install.packages("timsac")
    }
    if (!requireNamespace("x13binary", quietly = TRUE)) {
        install.packages("x13binary")
    }
    if (!requireNamespace("trend", quietly = TRUE)) {
        install.packages("trend")
    }
    library(season)
    library(seas)
    library(timsac)
    library(x13binary)
    library(trend)
''')

class SeasonalAdjustment:
    """
    Interface to perform seasonal adjustment techniques using various R packages through rpy2.
    """

    def __init__(self, data):
        """
        Initialize the SeasonalAdjustment object with the data.

        Args:
            data (pandas.DataFrame): The input data.
        """
        self.data = data

    def seasonal_decompose(self, method='stl'):
        """
        Perform seasonal decomposition.

        Args:
            method (str): The method to use for decomposition. Options: 'stl', 'seas', 'x11'. Default is 'stl'.

        Returns:
            dict: A dictionary containing trend, seasonal, and residual components.
        """
        seasonal_decompose_dict = {}
        if method == 'stl':
            result = robjects.r['stl'](self.data, s_window="periodic")
            seasonal_decompose_dict['trend'] = pd.Series(result.rx2('time.series')[0], index=self.data.index)
            seasonal_decompose_dict['seasonal'] = pd.Series(result.rx2('time.series')[1], index=self.data.index)
            seasonal_decompose_dict['residual'] = pd.Series(result.rx2('time.series')[2], index=self.data.index)
        elif method == 'seas':
            result = robjects.r['seas'](self.data)
            seasonal_decompose_dict['trend'] = pd.Series(result.rx2('trend'), index=self.data.index)
            seasonal_decompose_dict['seasonal'] = pd.Series(result.rx2('seasonal'), index=self.data.index)
            seasonal_decompose_dict['residual'] = pd.Series(result.rx2('irregular'), index=self.data.index)
        elif method == 'x11':
            result = robjects.r['x11'](self.data)
            seasonal_decompose_dict['trend'] = pd.Series(result.rx2('trend'), index=self.data.index)
            seasonal_decompose_dict['seasonal'] = pd.Series(result.rx2('seasonal'), index=self.data.index)
            seasonal_decompose_dict['residual'] = pd.Series(result.rx2('irregular'), index=self.data.index)
        else:
            raise ValueError("Invalid method. Supported methods are 'stl', 'seas', and 'x11'.")
        return seasonal_decompose_dict

    def census_x13_arima(self):
        """
        Perform seasonal adjustment using the X-13ARIMA-SEATS method.

        Returns:
            pandas.DataFrame: Seasonally adjusted data.
        """
        result = robjects.r['x13'](self.data)
        return pd.Series(result.rx2('seasadj'))

    def census_x11_arima(self):
        """
        Perform seasonal adjustment using the X-11 ARIMA method.

        Returns:
            pandas.DataFrame: Seasonally adjusted data.
        """
        result = robjects.r['x11'](self.data)
        return pd.Series(result.rx2('seasadj'))

    def census_seats(self):
        """
        Perform seasonal adjustment using the SEATS method.

        Returns:
            pandas.DataFrame: Seasonally adjusted data.
        """
        result = robjects.r['seas'](self.data, method="Seats")
        return pd.Series(result.rx2('seasonal'))

    def timsac(self):
        """
        Perform seasonal adjustment using the TRAMO-SEATS method.

        Returns:
            pandas.DataFrame: Seasonally adjusted data.
        """
        result = robjects.r['timsac'](self.data)
        return pd.Series(result.rx2('final'))

    def census_seasonal(self):
        """
        Perform seasonal adjustment using the CENSUS X-12-ARIMA method.

        Returns:
            pandas.DataFrame: Seasonally adjusted data.
        """
        result = robjects.r['seasonal'](self.data)
        return pd.Series(result.rx2('adjusted'))

# Example usage:
# data = pd.Series([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
# seasonal_adjustment = SeasonalAdjustment(data)
# decomposition_stl = seasonal_adjustment.seasonal_decompose(method='stl')
# decomposition_seas = seasonal_adjustment.seasonal_decompose(method='seas')
# decomposition_x11 = seasonal_adjustment.seasonal_decompose(method='x11')
# x13_arima = seasonal_adjustment.census_x13_arima()
# x11_arima = seasonal_adjustment.census_x11_arima()
# seats = seasonal_adjustment.census_seats()
# tramoseats = seasonal_adjustment.timsac()
# x12_arima = seasonal_adjustment.census_seasonal()
