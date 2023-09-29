#importing the Dependencies
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from scipy import stats


#data collection & Analysis
# Loading the data from csv file to a Pandas Dataframe
#customer_data = pd.read_csv("C:/Users/omc/Desktop/Task1/data.csv", encoding="unicode_escape")
customer_data = pd.read_csv("C:/Users/omc/Desktop/Task/data.csv",encoding="unicode_escape")

#first 5rows in the dataframe
# Finding the number of rows and columns
customer_data.head()
print(customer_data.head())


# finding the number of rows and columns
customer_data.shape

# Getting some information about the dataset
customer_data.info()

# checking for misiing values
customer_data.isnull().sum()
print(customer_data.isnull().sum())

#Choosing the annual income columns & spending score column
X = customer_data.iloc[:,[3,4]].values
print(X)

