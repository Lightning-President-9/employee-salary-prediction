# Employee Salary Prediction – Interactive Dashboard

An interactive machine learning–based dashboard for predicting employee salary categories using demographic and employment attributes from the Adult Census Income dataset.

This project integrates data preprocessing, supervised machine learning, and interactive visualization to present income predictions in an intuitive and responsive web-based dashboard.

---

## Project Overview

This is a personal project developed to explore how machine learning classification models can be applied to socio-economic and employment datasets.

A supervised classification model is trained on the Adult Census Income dataset and used to predict whether an individual’s income falls into the **≤50K** or **>50K** category based on demographic and work-related attributes.  
The results are presented through interactive Plotly visualizations in a Flask-based web dashboard.

---

## Predicted Output

The dashboard predicts the following salary categories:

- **≤50K**
- **>50K**

Predictions are generated based on multiple demographic and employment-related input features.

---

## Input Features Used

The model uses the following attributes from the Adult Census dataset:

- Age  
- Workclass  
- Final Weight (fnlwgt)  
- Education  
- Educational Number  
- Marital Status  
- Occupation  
- Relationship  
- Race  
- Gender  
- Capital Gain  
- Capital Loss  
- Hours per Week  
- Native Country  

(Target variable: `income`)

---

## Dashboard Features

- Interactive salary prediction based on user inputs  
- Dynamic input form generated from model encoders  
- Sample placeholder data for quick testing  
- Interactive visualizations using pre-generated Plotly JSON:
  - Income distribution
  - Age vs income comparison
  - Education vs income comparison  
- Responsive, dashboard-style UI  

---

## Machine Learning Model

- **Model Type:** Supervised Classification  
- **Algorithms:** scikit-learn classifiers  
- **Training Environment:** Jupyter Notebook  
- **Approach:**
  - Data cleaning and preprocessing  
  - Label encoding for categorical variables  
  - Feature scaling (where applicable)  
  - Model training and evaluation  
  - Serialization using `joblib`  

---

## Dataset

- **Source:** Kaggle  
- **Link:** https://www.kaggle.com/datasets/uciml/adult-census-income  
- **Description:** Demographic and employment data used to predict income levels.

---

## Jupyter Notebook

Model training, exploratory data analysis, and evaluation are documented in the notebook:

https://github.com/Lightning-President-9/Employee-Salary-Prediction_Rohit-Wachnekar/blob/main/Employee_Salary_Prediction.ipynb

---

## GitHub Repositories

- **Main Project Repository:**  
  https://github.com/Lightning-President-9/Employee-Salary-Prediction_Rohit-Wachnekar

- **Flask Deployment Repository:**  
  https://github.com/Lightning-President-9/employee-salary-prediction

---

## Tech Stack

- **Backend:** Flask (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **Visualization:** Plotly  
- **Machine Learning:** scikit-learn  
- **Model Persistence:** joblib  

---

## ⚠ Disclaimer

This project is a personal academic and learning project.

Predictions are indicative only and are based on historical data and machine learning models.  
They must not be used for employment, compensation, or policy decision-making and should not replace professional or legal evaluation.