__version__='0.1.1'
__author__ ='Matan Carmon'
__date__ = November 2023'

import pandas as pd
import rpy2.robjects.packages as rpackages
from rpy2.robjects import pandas2ri

# Activate automatic conversion of pandas objects to R objects
pandas2ri.activate()

# Install and import necessary R packages
utils = rpackages.importr('utils')
utils.chooseCRANmirror(ind=1)

# Install R packages
packages = ['cluster', 'dbscan', 'mclust']
utils.install_packages(rpackages.StrVector(packages))

# Import required R libraries
cluster = rpackages.importr('cluster')
dbscan = rpackages.importr('dbscan')
mclust = rpackages.importr('mclust')

class UnsupervisedModels:
    """
    Interface to perform unsupervised learning using various R packages through rpy2.
    """

    def __init__(self, data):
        """
        Initialize the UnsupervisedModels object with the data.

        Args:
            data (pandas.DataFrame): The input data.
        """
        self.data = data

    def kmeans(self, centers=3):
        """
        Perform clustering using K-Means algorithm.

        Args:
            centers (int): The number of clusters. Default is 3.

        Returns:
            R object: The K-Means clustering model.
        """
        kmeans_fit = cluster.kmeans(self.data, centers=centers)
        return kmeans_fit

    def pam(self, k=3):
        """
        Perform clustering using Partitioning Around Medoids (PAM).

        Args:
            k (int): The number of clusters. Default is 3.

        Returns:
            R object: The PAM clustering model.
        """
        pam_fit = cluster.pam(self.data, k=k)
        return pam_fit

    def dbscan(self, eps=0.5, minPts=5):
        """
        Perform clustering using DBSCAN algorithm.

        Args:
            eps (float): The maximum distance between two samples for one to be considered as in the neighborhood
                of the other. Default is 0.5.
            minPts (int): The number of samples in a neighborhood for a point to be considered as a core point.
                Default is 5.

        Returns:
            R object: The DBSCAN clustering model.
        """
        dbscan_fit = dbscan.dbscan(self.data, eps=eps, MinPts=minPts)
        return dbscan_fit

    def mclust(self):
        """
        Perform clustering using Mclust algorithm.

        Returns:
            R object: The Mclust clustering model.
        """
        mclust_fit = mclust.Mclust(self.data)
        return mclust_fit

# Example usage:
# data = pd.DataFrame({'feature1': [1, 2, 3, 4, 5],
#                      'feature2': [10, 15, 20, 25, 30]})
# unsupervised_models = UnsupervisedModels(data)
# kmeans_model = unsupervised_models.kmeans()
# pam_model = unsupervised_models.pam()
# dbscan_model = unsupervised_models.dbscan()
# mclust_model = unsupervised_models.mclust()
