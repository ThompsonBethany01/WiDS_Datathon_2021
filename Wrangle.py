# Project: Wids Datathon 2021 - Predicting Diabetes in ICU Patients
# File: Wrangle.py
# Author: Bethany Thompson
# Date: January 2021
'''
Functions to read data from a csv file to a pandas dataframe ready for the next steps in exploration.
'''

# import needed to run functions 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

############################################## Wrangle Function ##############################################

def wrangle_data():

    # reading csv file from data folder in same main directory into a pandas dataframe
    df = pd.read_csv('data/TrainingWiDS2021.csv', index_col=0)

    return prepped_df

############################################## Helper Functions ##############################################

# functions called within the main wrangle data function

def convert_data_types(df):

    '''
    Converting columns to correct data types, such as age being 24.0 to 24. Nulls can not be converted, so
    are filled with the average value.
    '''

    # Converting ages to integers without trailing decimals of .0
    # Setting avariable as rounded average age
    avg_age = round(df.age.mean(),0)

    # Filling null values with the average age
    df.age = df.age.fillna(avg_age)

    # Age is in years, and all values end in 0 - will be converted to integers
    df.age = df.astype({'age':'int'})

    return df

def create_dummies(df):
    