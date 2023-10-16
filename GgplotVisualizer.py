__version__='0.0.32'
__author__ ='Matan Carmon'
__date__ = 'October 2023'

import pandas as pd
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import importr

# Activate automatic conversion of pandas objects to R objects
pandas2ri.activate()

# Load the ggplot2 package
ggplot2 = importr('ggplot2')

class GgplotVisualizer:
    """
    Interface to create visualizations using ggplot through rpy2.
    """

    def __init__(self, data):
        """
        Initialize the GgplotVisualizer object with the data.

        Args:
            data (pandas.DataFrame): The input data.
        """
        self.data = data

    def scatterplot(self, x, y, **kwargs):
        """
        Create a scatterplot.

        Args:
            x (str): The column name for the x-axis.
            y (str): The column name for the y-axis.
            kwargs: Additional arguments to pass to ggplot.

        Returns:
            R object: The ggplot object.
        """
        p = ggplot2.ggplot(self.data) + ggplot2.aes_string(x=x, y=y) + ggplot2.geom_point(**kwargs)
        return p

    def lineplot(self, x, y, **kwargs):
        """
        Create a line plot.

        Args:
            x (str): The column name for the x-axis.
            y (str): The column name for the y-axis.
            kwargs: Additional arguments to pass to ggplot.

        Returns:
            R object: The ggplot object.
        """
        p = ggplot2.ggplot(self.data) + ggplot2.aes_string(x=x, y=y) + ggplot2.geom_line(**kwargs)
        return p

    def histogram(self, x, **kwargs):
        """
        Create a histogram.

        Args:
            x (str): The column name for the x-axis.
            kwargs: Additional arguments to pass to ggplot.

        Returns:
            R object: The ggplot object.
        """
        p = ggplot2.ggplot(self.data) + ggplot2.aes_string(x=x) + ggplot2.geom_histogram(**kwargs)
        return p

    def boxplot(self, x, y, **kwargs):
        """
        Create a boxplot.

        Args:
            x (str): The column name for the x-axis (typically categorical).
            y (str): The column name for the y-axis (typically numerical).
            kwargs: Additional arguments to pass to ggplot.

        Returns:
            R object: The ggplot object.
        """
        p = ggplot2.ggplot(self.data) + ggplot2.aes_string(x=x, y=y) + ggplot2.geom_boxplot(**kwargs)
        return p

    def barplot(self, x, y, **kwargs):
        """
        Create a bar plot.

        Args:
            x (str): The column name for the x-axis (typically categorical).
            y (str): The column name for the y-axis (typically numerical).
            kwargs: Additional arguments to pass to ggplot.

        Returns:
            R object: The ggplot object.
        """
        p = ggplot2.ggplot(self.data) + ggplot2.aes_string(x=x, y=y) + ggplot2.geom_bar(stat="identity", **kwargs)
        return p

    def densityplot(self, x, **kwargs):
        """
        Create a density plot.

        Args:
            x (str): The column name for the x-axis.
            kwargs: Additional arguments to pass to ggplot.

        Returns:
            R object: The ggplot object.
        """
        p = ggplot2.ggplot(self.data) + ggplot2.aes_string(x=x) + ggplot2.geom_density(**kwargs)
        return p

    def violinplot(self, x, y, **kwargs):
        """
        Create a violin plot.

        Args:
            x (str): The column name for the x-axis (typically categorical).
            y (str): The column name for the y-axis (typically numerical).
            kwargs: Additional arguments to pass to ggplot.

        Returns:
            R object: The ggplot object.
        """
        p = ggplot2.ggplot(self.data) + ggplot2.aes_string(x=x, y=y) + ggplot2.geom_violin(**kwargs)
        return p

    def scatter_matrix(self, **kwargs):
        """
        Create a scatterplot matrix.

        Args:
            kwargs: Additional arguments to pass to ggplot.

        Returns:
            R object: The ggplot object.
        """
        p = ggplot2.ggpairs(self.data, **kwargs)
        return p

# Example usage:
# df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
#                    'B': [10, 15, 20, 25, 30],
#                    'C': ['X', 'Y', 'X', 'Y', 'X']})
# ggplot_visualizer = GgplotVisualizer(df)
# scatterplot = ggplot_visualizer.scatterplot('A', 'B')
# lineplot = ggplot_visualizer.lineplot('A', 'B', color="'blue'")
# histogram = ggplot_visualizer.histogram('A', fill="'green'")
# boxplot = ggplot_visualizer.boxplot('C', 'B', fill="'red'")
# barplot = ggplot_visualizer.barplot('C', 'B', fill="'orange'")
# densityplot = ggplot_visualizer.densityplot('B', fill="'yellow'")
# violinplot = ggplot_visualizer.violinplot('C', 'B', fill="'purple'")
# scatter_matrix = ggplot_visualizer.scatter_matrix()
