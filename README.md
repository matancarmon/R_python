# Machine Learning and Data Analysis with R in Python (Author: Matan Carmon)

This repository contains Python code that leverages R's machine learning capabilities, statistical analysis, and visualization techniques through the `rpy2` package. `rpy2` allows seamless integration between Python and R, enabling you to utilize R's extensive ecosystem of packages for various tasks within Python scripts.

## Getting Started

### Prerequisites

- Python 3.x
- R
- `rpy2` Python package
- Necessary R packages (automatically installed by the Python scripts)

### Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/rpy2-machine-learning.git
    ```

2. Navigate to the cloned directory:

    ```bash
    cd rpy2-machine-learning
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Ensure that R is installed and accessible from your system's PATH.

## Usage

### Classification

To perform classification using various models, navigate to the `classification` directory:

```bash
cd classification
```

Execute the Python script of your choice. For example:

```bash
python random_forest_classification.py
```

The script will execute the chosen classification model using sample data and print the results.

### Unsupervised Learning

To perform unsupervised learning using different models, navigate to the `unsupervised_learning` directory:

```bash
cd unsupervised_learning
```

Execute the Python script corresponding to the desired unsupervised learning algorithm:

```bash
python kmeans_clustering.py
```

The script will run the chosen unsupervised learning model on sample data and display the results.

### Seasonal Adjustment

To perform seasonal adjustment techniques using R's packages, navigate to the `seasonal_adjustment` directory:

```bash
cd seasonal_adjustment
```

Execute the Python script corresponding to the desired seasonal adjustment method:

```bash
python x13_seasonal_adjustment.py
```

The script will perform seasonal adjustment using the X-13ARIMA-SEATS method on sample data and display the results.

### Visualization

To create visualizations using ggplot through rpy2, navigate to the `visualization` directory:

```bash
cd visualization
```

Execute the Python script corresponding to the desired visualization:

```bash
python scatterplot.py
```

The script will create a scatter plot using ggplot2 and display the visualization.

## Models and Analysis Available

### Classification Models

- Random Forest
- Support Vector Machines (SVM)
- Logistic Regression
- Decision Trees
- Neural Network
- K-Nearest Neighbors (K-NN)
- Naive Bayes

### Unsupervised Learning Models

- K-Means Clustering
- Partitioning Around Medoids (PAM)
- DBSCAN
- Mclust

### Seasonal Adjustment Techniques

- X-13ARIMA-SEATS
- SEATS
- TRAMO-SEATS
- CENSUS X-12-ARIMA
- STL

### Visualization Techniques

- Scatter Plots
- Line Plots
- Histograms
- Box Plots
- Bar Plots
- Density Plots
- Violin Plots
- Scatterplot Matrices

## Contributing

Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, please submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---
