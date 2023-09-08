"""rpy2_stats - A Python package for advanced statistical functions and models in python"""

import rpy2.robjects as robjects

__version__ = '0.1.0'
__author__ = 'Matan Carmon'
__date__ = 'September 2023'

# utils.py
"""Module containing common statistical functions"""

def mean(data):
    """Calculate the mean of a numeric vector using R's mean function."""
    r_mean = robjects.r['mean']
    return r_mean(robjects.FloatVector(data))[0]

def variance(data):
    """Calculate the variance of a numeric vector using R's var function."""
    r_var = robjects.r['var']
    return r_var(robjects.FloatVector(data))[0]

def median(data):
    """Calculate the median of a numeric vector using R's median function."""
    r_median = robjects.r['median']
    return r_median(robjects.FloatVector(data))[0]

def quantile(data, probs=[0.25, 0.5, 0.75]):
    """Calculate the quantiles of a numeric vector using R's quantile function."""
    r_quantile = robjects.r['quantile']
    quantiles = r_quantile(robjects.FloatVector(data), probs=probs)
    return dict(zip(probs, quantiles))

def correlation(x, y):
    """Calculate the correlation coefficient between two numeric vectors."""
    r_cor = robjects.r['cor']
    corr = r_cor(robjects.FloatVector(x), robjects.FloatVector(y))
    return corr[0]

def boxplot(data):
    """Generate a boxplot for a numeric vector."""
    r_boxplot = robjects.r['boxplot']
    r_boxplot(robjects.FloatVector(data))

def histogram(data):
    """Generate a histogram for a numeric vector."""
    r_hist = robjects.r['hist']
    r_hist(robjects.FloatVector(data))

def density(data):
    """Generate a density plot for a numeric vector."""
    r_density = robjects.r['density']
    r_density(robjects.FloatVector(data))

def t_test(x, y):
    """Perform a two-sample t-test."""
    r_t_test = robjects.r['t.test']
    result = r_t_test(robjects.FloatVector(x), robjects.FloatVector(y))
    return result

def anova(formula, data):
    """Perform an analysis of variance."""
    r_anova = robjects.r['anova']
    result = r_anova(robjects.Formula(formula), data=data)
    return result

def wilcox_test(x, y):
    """Perform a Wilcoxon rank sum test."""
    r_wilcox_test = robjects.r['wilcox.test']
    result = r_wilcox_test(robjects.FloatVector(x), robjects.FloatVector(y))
    return result

def kruskal_test(x, y):
    """Perform a Kruskal-Wallis rank sum test."""
    r_kruskal_test = robjects.r['kruskal.test']
    result = r_kruskal_test(robjects.FloatVector(x), robjects.FloatVector(y))
    return result

def chi_square_test(x, y):
    """Perform a chi-square test of independence."""
    r_chisq_test = robjects.r['chisq.test']
    result = r_chisq_test(robjects.FloatVector(x), robjects.FloatVector(y))
    return result

def fisher_exact_test(x, y):
    """Perform Fisher's exact test."""
    r_fisher_test = robjects.r['fisher.test']
    result = r_fisher_test(robjects.FloatVector(x), robjects.FloatVector(y))
    return result

# models.py
"""Module containing statistical models"""

def linear_regression(x, y):
    """Perform linear regression using R's lm function."""
    r_lm = robjects.r['lm']
    formula = robjects.Formula('y ~ x')
    data = robjects.DataFrame({'x': robjects.FloatVector(x), 'y': robjects.FloatVector(y)})
    lm_result = r_lm(formula, data=data)
    return lm_result

def generalized_linear_model(formula, data, family="gaussian"):
    """Perform generalized linear modeling using R's glm function."""
    r_glm = robjects.r['glm']
    r_family = robjects.r[family]
    formula = robjects.Formula(formula)
    glm_result = r_glm(formula, data=data, family=r_family())
    return glm_result

def time_series_forecasting(data, frequency=12, method="auto"):
    """Perform time series forecasting using R's forecast package."""
    r_forecast = robjects.r['forecast']
    r_ts = robjects.r['ts']
    ts_data = r_ts(robjects.FloatVector(data), frequency=frequency)
    forecast_result = r_forecast(ts_data, method=method)
    return forecast_result

def arima_model(data, order=(1, 1, 1)):
    """Fit an ARIMA model to a time series using R's forecast package."""
    r_arima = robjects.r['arima']
    r_ts = robjects.r['ts']
    ts_data = r_ts(robjects.FloatVector(data))
    arima_result = r_arima(ts_data, order=robjects.IntVector(order))
    return arima_result

def pca(data, scale=True):
    """Perform principal component analysis (PCA) using R's prcomp function."""
    r_prcomp = robjects.r['prcomp']
    result = r_prcomp(data, scale=scale)
    return result

def hierarchical_clustering(data, method="complete"):
    """Perform hierarchical clustering using R's hclust function."""
    r_hclust = robjects.r['hclust']
    result = r_hclust(data, method=method)
    return result

# dataframe.py
"""Module for data frame manipulation"""

def filter_data(data, condition):
    """Filter data frame based on a condition."""
    r_filter = robjects.r['filter']
    filtered_data = r_filter(data, condition)
    return filtered_data

def mutate(data, **kwargs):
    """Add new columns or modify existing ones in the data frame."""
    r_mutate = robjects.r['mutate']
    mutated_data = data
    for column, value in kwargs.items():
        mutated_data = r_mutate(mutated_data, **{column: value})
    return mutated_data

def summarize(data, **kwargs):
    """Summarize data frame by calculating summary statistics."""
    r_summarize = robjects.r['summary']
    summarized_data = r_summarize(data, **kwargs)
    return summarized_data

def group_by(data, columns):
    """Group data frame by specified columns."""
    r_group_by = robjects.r['group_by']
    grouped_data = r_group_by(data, *columns)
    return grouped_data

def summarize_grouped(data):
    """Summarize grouped data frame."""
    r_summarize = robjects.r['summarize']
    summarized_data = r_summarize(data)
    return summarized_data

def arrange(data, *columns, desc=False):
    """Arrange rows of data frame by specified columns."""
    r_arrange = robjects.r['arrange']
    arranged_data = r_arrange(data, *columns, desc=desc)
    return arranged_data

def select(data, *columns):
    """Select columns from data frame."""
    r_select = robjects.r['select']
    selected_data = r_select(data, *columns)
    return selected_data

def distinct(data, *columns):
    """Select distinct rows from data frame."""
    r_distinct = robjects.r['distinct']
    distinct_data = r_distinct(data, *columns)
    return distinct_data

def inner_join(data1, data2, by):
    """Perform inner join between two data frames."""
    r_inner_join = robjects.r['inner_join']
    joined_data = r_inner_join(data1, data2, by=by)
    return joined_data

def left_join(data1, data2, by):
    """Perform left join between two data frames."""
    r_left_join = robjects.r['left_join']
    joined_data = r_left_join(data1, data2, by=by)
    return joined_data

def right_join(data1, data2, by):
    """Perform right join between two data frames."""
    r_right_join = robjects.r['right_join']
    joined_data = r_right_join(data1, data2, by=by)
    return joined_data

def full_join(data1, data2, by):
    """Perform full join between two data frames."""
    r_full_join = robjects.r['full_join']
    joined_data = r_full_join(data1, data2, by=by)
    return joined_data

def pivot_longer(data, cols, names_to="name", values_to="value"):
    """Convert data from wide to long format."""
    r_pivot_longer = robjects.r['pivot_longer']
    long_data = r_pivot_longer(data, cols, names_to=names_to, values_to=values_to)
    return long_data

def pivot_wider(data, names_from="name", values_from="value"):
    """Convert data from long to wide format."""
    r_pivot_wider = robjects.r['pivot_wider']
    wide_data = r_pivot_wider(data, names_from=names_from, values_from=values_from)
    return wide_data
