__version__='0.0.2'
__author__ ='Matan Carmon'
__date__ = November 2023'


import pandas as pd
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri

# Activate automatic conversion of pandas objects to R objects
pandas2ri.activate()

# Install and import necessary R packages
# Make sure to install these packages in your R environment before running this code
# Example: install.packages(c("nnet", "class", "kernlab"))
robjects.r('''
    if (!requireNamespace("nnet", quietly = TRUE)) {
        install.packages("nnet")
    }
    if (!requireNamespace("class", quietly = TRUE)) {
        install.packages("class")
    }
    if (!requireNamespace("kernlab", quietly = TRUE)) {
        install.packages("kernlab")
    }
    library(nnet)
    library(class)
    library(kernlab)
''')

class ClassificationModels:
    """
    Interface to perform classification using various R packages through rpy2.
    """

    def __init__(self, data, target):
        """
        Initialize the ClassificationModels object with the data and target variable.

        Args:
            data (pandas.DataFrame): The input data.
            target (str): The target variable name.
        """
        self.data = data
        self.target = target

    def random_forest(self, ntree=500, mtry=None):
        """
        Perform classification using Random Forest.

        Args:
            ntree (int): The number of trees in the forest. Default is 500.
            mtry (int or str): The number of variables randomly sampled as candidates at each split. 
                If None, mtry is set to the square root of the number of predictors.

        Returns:
            R object: The random forest model.
        """
        formula = robjects.Formula(f'{self.target} ~ .')
        rf_fit = robjects.r['randomForest'](formula, data=self.data, ntree=ntree, mtry=mtry)
        return rf_fit

    def svm(self, kernel='radial', cost=1):
        """
        Perform classification using Support Vector Machines (SVM).

        Args:
            kernel (str): The kernel type. Options: 'linear', 'polynomial', 'radial', 'sigmoid'. Default is 'radial'.
            cost (float): The cost parameter for the SVM. Default is 1.

        Returns:
            R object: The SVM model.
        """
        formula = robjects.Formula(f'{self.target} ~ .')
        svm_fit = robjects.r['svm'](formula, data=self.data, kernel=kernel, cost=cost)
        return svm_fit

    def logistic_regression(self):
        """
        Perform classification using Logistic Regression.

        Returns:
            R object: The logistic regression model.
        """
        formula = robjects.Formula(f'{self.target} ~ .')
        logit_fit = robjects.r['glm'](formula, data=self.data, family="binomial")
        return logit_fit

    def decision_tree(self):
        """
        Perform classification using Decision Trees.

        Returns:
            R object: The decision tree model.
        """
        formula = robjects.Formula(f'{self.target} ~ .')
        dt_fit = robjects.r['rpart'](formula, data=self.data)
        return dt_fit

    def neural_network(self, size=(5, 2)):
        """
        Perform classification using Neural Network.

        Args:
            size (tuple): Number of units in the hidden layers. Default is (5, 2).

        Returns:
            R object: The neural network model.
        """
        formula = robjects.Formula(f'{self.target} ~ .')
        nn_fit = robjects.r['nnet'](formula, data=self.data, size=size)
        return nn_fit

    def k_nearest_neighbors(self, k=5):
        """
        Perform classification using K-Nearest Neighbors (K-NN).

        Args:
            k (int): Number of neighbors to consider. Default is 5.

        Returns:
            R object: The K-NN model.
        """
        knn_fit = robjects.r['knn'](self.data, self.target, k=k)
        return knn_fit

    def naive_bayes(self):
        """
        Perform classification using Naive Bayes.

        Returns:
            R object: The Naive Bayes model.
        """
        formula = robjects.Formula(f'{self.target} ~ .')
        nb_fit = robjects.r['naiveBayes'](formula, data=self.data)
        return nb_fit

# Example usage:
# data = pd.DataFrame({'feature1': [1, 2, 3, 4, 5],
#                      'feature2': [10, 15, 20, 25, 30],
#                      'target': [0, 1, 0, 1, 0]})
# classification_models = ClassificationModels(data, target='target')
# rf_model = classification_models.random_forest()
# svm_model = classification_models.svm()
# logit_model = classification_models.logistic_regression()
# dt_model = classification_models.decision_tree()
# nn_model = classification_models.neural_network()
# knn_model = classification_models.k_nearest_neighbors()
# nb_model = classification_models.naive_bayes()
