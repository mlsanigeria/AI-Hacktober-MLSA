

# GPA Prediction Readme

This readme provides an overview of the project for predicting GPA (CGPA).

## Table of Contents
- [Project Description](#project-description)
- [Data Importation](#data-importation)
- [Data Preprocessing](#data-preprocessing)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Data Transformation](#data-transformation)
- [Feature Engineering](#feature-engineering)
- [Data Splitting](#data-splitting)
- [Model Development and Evaluation](#model-development-and-evaluation)
- [Model Selection and Performance](#model-selection-and-performance)

### Project Description

The project's primary objective is to predict the Grade Point Average (CGPA) of students based on various features provided in the dataset. These features include academic performance, demographic information, study habits, and more. The project uses machine learning regression models to predict CGPA and evaluate their performance.

### Data Importation

In this step, the required libraries and dependencies are imported, and the dataset is loaded from the 'year_gpa.xlsx' Excel file. The dataset is then examined, and its structure is understood.

### Data Preprocessing

Data preprocessing is a crucial step to ensure that the dataset is clean and ready for modeling. This step includes renaming columns, handling missing values, and converting data types. Several columns are mapped from string values to numerical representations, and outliers are addressed. The dataset is prepared for further analysis.

### Exploratory Data Analysis (EDA)

EDA is performed to gain insights into the dataset. The distribution of CGPA, relationships between numerical variables, and visualizations of categorical features are presented. EDA helps to understand the data and identify potential patterns.

### Data Transformation

Categorical features are encoded using Label Encoding, and specific columns are mapped to numerical values. Additionally, a feature is created to represent the total study time, combining the 'Days_per_week_for_reading' and 'Hours_per_day_for_personal_study' columns.

### Feature Engineering

A new feature is introduced to the dataset to capture the total study time. This feature can potentially provide additional information for modeling.

### Data Splitting

The dataset is split into training and testing sets, which are essential for training and evaluating machine learning models. A 70-30 split ratio is used.

### Model Development and Evaluation

Various machine learning regression models are developed and evaluated to predict CGPA. Models include Linear Regression, Lasso, Ridge, K-Nearest Neighbors, Support Vector Machine, Decision Tree, Random Forest, and more. The root mean squared error (RMSE) is used to evaluate each model's performance.

### Model Selection and Performance

The LightGBM model is selected based on its best performance, and hyperparameters are tuned to optimize its predictive power. The final model is trained on the entire dataset and tested on the testing set, achieving an RMSE that indicates its predictive accuracy.
