__author__="Matan Carmon"
__date__="September 2023"

import pandas as pd
import numpy as np
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri

# Activate automatic conversion of pandas objects to R objects
pandas2ri.activate()

class RFunctions:
    """
    Interface to apply R functions on Pandas DataFrame or Series.
    """

    def __init__(self, data):
        """
        Initialize the RFunctions object with the data.

        Args:
            data (pandas.DataFrame or pandas.Series): The input data.
        """
        self.data = data

    def mean(self):
        """
        Calculate the mean of the data.

        Returns:
            float: The mean value.
        """
        return self._apply_r_function('mean')

    def variance(self):
        """
        Calculate the variance of the data.

        Returns:
            float: The variance value.
        """
        return self._apply_r_function('variance')

    def median(self):
        """
        Calculate the median of the data.

        Returns:
            float: The median value.
        """
        return self._apply_r_function('median')

    def quantile(self, probs=[0.25, 0.5, 0.75]):
        """
        Calculate the quantiles of the data.

        Args:
            probs (list): List of probabilities for quantiles. Default is [0.25, 0.5, 0.75].

        Returns:
            dict: Dictionary containing quantile values.
        """
        return self._apply_r_function_with_args('quantile', probs)

    def correlation(self, other=None):
        """
        Calculate the correlation between two datasets.

        Args:
            other (pandas.DataFrame or pandas.Series, optional): The other dataset to calculate correlation with.
                If not provided, calculates correlation with self.data.

        Returns:
            float: The correlation coefficient.
        """
        if other is None:
            other = self.data
        return self._apply_r_function_with_other('correlation', other)

    def t_test(self, other):
        """
        Perform a two-sample t-test between two datasets.

        Args:
            other (pandas.Series or array-like): The other dataset for t-test.

        Returns:
            R object: Result of the t-test.
        """
        return self._apply_r_function_with_other('t_test', other)

    def linear_regression(self, y):
        """
        Perform linear regression.

        Args:
            y (pandas.Series or array-like): The dependent variable for regression.

        Returns:
            R object: Result of linear regression.
        """
        return self._apply_r_function_with_other('linear_regression', y)

    def generalized_linear_model(self, formula, family="gaussian"):
        """
        Perform generalized linear modeling.

        Args:
            formula (str): Formula specifying the model.
            family (str, optional): The family of the distribution. Default is "gaussian".

        Returns:
            R object: Result of generalized linear modeling.
        """
        return self._apply_r_function_with_args('generalized_linear_model', formula, family)

    def pca(self, scale=True):
        """
        Perform principal component analysis (PCA).

        Args:
            scale (bool, optional): Whether to scale the data. Default is True.

        Returns:
            R object: Result of PCA.
        """
        return self._apply_r_function_with_args('pca', scale)

    def hierarchical_clustering(self, method="complete"):
        """
        Perform hierarchical clustering.

        Args:
            method (str, optional): The method to use for clustering. Default is "complete".

        Returns:
            R object: Result of hierarchical clustering.
        """
        return self._apply_r_function_with_args('hierarchical_clustering', method)

    def _apply_r_function(self, func_name, *args):
        """
        Internal method to apply an R function on the data.

        Args:
            func_name (str): Name of the R function to apply.
            args: Additional arguments for the function.

        Returns:
            Depends on the function called.
        """
        r_func = robjects.r[func_name]
        if isinstance(self.data, pd.DataFrame):
            self.data = pandas2ri.py2ri(self.data)
        if args:
            return r_func(self.data, *args)
        else:
            return r_func(self.data)

    def _apply_r_function_with_args(self, func_name, *args):
        """
        Internal method to apply an R function with arguments on the data.

        Args:
            func_name (str): Name of the R function to apply.
            args: Arguments for the function.

        Returns:
            Depends on the function called.
        """
        r_func = robjects.r[func_name]
        if isinstance(self.data, pd.DataFrame):
            self.data = pandas2ri.py2ri(self.data)
        return r_func(self.data, *args)

    def _apply_r_function_with_other(self, func_name, other):
        """
        Internal method to apply an R function with another dataset on the data.

        Args:
            func_name (str): Name of the R function to apply.
            other (pandas.DataFrame or pandas.Series): The other dataset.

        Returns:
            Depends on the function called.
        """
        r_func = robjects.r[func_name]
        if isinstance(self.data, pd.DataFrame):
            self.data = pandas2ri.py2ri(self.data)
        if isinstance(other, pd.DataFrame):
            other = pandas2ri.py2ri(other)
        return r_func(self.data, other)

class DataFrameInterface:
    """
    Interface to call R functions on Pandas DataFrame or Series.
    """

    def __init__(self, data):
        """
        Initialize the DataFrameInterface object with the data.

        Args:
            data (pandas.DataFrame or pandas.Series): The input data.
        """
        self.data = data

    def __getitem__(self, item):
        """
        Get the RFunctions object for a specific column or columns of the DataFrame.

        Args:
            item (str or tuple): The column name or tuple of column names.

        Returns:
            RFunctions: The RFunctions object for the specified column or columns.
        """
        if isinstance(item, tuple):
            return RFunctions(self.data[list(item)])
        else:
            return RFunctions(self.data[item])

    def __getattr__(self, item):
        """
        Get attribute from RFunctions object.

        Args:
            item (str): The attribute name.

        Returns:
            Any: The attribute value.
        """
        if hasattr(RFunctions, item):
            return getattr(RFunctions(self.data), item)
        else:
            raise AttributeError(f"'DataFrameInterface' object has no attribute '{item}'")

# Example usage:
# df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
# df_interface = DataFrameInterface(df)
# print(df_interface['A'].mean())
# print(df_interface.mean())
# print(df_interface['A','B'].correlation())
# print(df_interface.linear_regression(df['A']))
# print(df_interface.generalized_linear_model('A ~ B + C'))
# print(df_interface.pca())
# print(df_interface.hierarchical_clustering())
