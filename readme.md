# Bangalore House Price Prediction
This project focuses on predicting house prices in Bangalore using machine learning. The dataset undergoes a thorough cleaning and preparation process before being utilized to train multiple models. The goal is to identify the best-performing model for accurate house price predictions. Additionally, a user-friendly UI is implemented using Python Streamlit, allowing users to input square footage, number of bathrooms, bedrooms, and the location of the Bangalore area to obtain an estimated cost of the house.

Table of Contents
1. Dataset
2. Data Cleaning and Preparation
3. Model Training
4. Best Model Selection
5. User Interface with Streamlit
6. Usage


## Dataset
The dataset used for this project contains information about house features such as square footage, number of bathrooms, bedrooms, and the location in Bangalore. It serves as the foundation for training machine learning models.

## Data Cleaning and Preparation
The dataset undergoes thorough cleaning and preparation to handle missing values, outliers, and ensure compatibility with machine learning algorithms.

## Model Training
Multiple machine learning models are trained on the prepared dataset. These models include linear regression, decision tree, and other regression algorithms to predict house prices accurately.

## Best Model Selection
The models' performance is evaluated, and the best-performing model is selected based on metrics such as mean squared error, R-squared, or other relevant evaluation criteria.

## User Interface with Streamlit
A user-friendly interface is developed using Python Streamlit. The UI allows users to input details such as square footage, number of bathrooms, bedrooms, and the location of the Bangalore area. It then provides an estimated cost of the house based on the trained machine learning model.

## Usage
### To use the project:

#### Clone the repository: git clone 
```
https://github.com/Rajkumar0819/BangaloreHousePricePrediction.git
```
#### Install dependencies: 
Create a virtual environment venv
```
pip install -r requirements.txt
```

#### Run the Streamlit app: 
```
streamlit run app.py
````
