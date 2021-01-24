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

    df = convert_data_types(df)

    df = create_dummies(df)

    df = remove_nulls(df)

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

    # Converting Apache 2 Diagnosis to integers without trailing .0
    # Setting variable as the average value
    apache_2_diagnosis_mean = df.apache_2_diagnosis.mean()

    # Filling the 1,685 null values with the average
    df.apache_2_diagnosis = df.apache_2_diagnosis.fillna(apache_2_diagnosis_mean)

    # Converting the data types to integers without trailing decimals
    df.apache_2_diagnosis = df.apache_2_diagnosis.astype('int')

    return df

def create_dummies(df):
    
    '''
    Convert categorical string/object variables to numerical categories
    '''

    # creating dummy variable for if patient is female
    df['is_female'] = df.gender.replace({'M':0, 'F':1})

    # converting icu stay types to corresponding values of 1, 2 and 3
    df.icu_stay_type = df.icu_stay_type.replace({'admit':1, 'transfer':2, 'readmit':3})

    return df

def remove_nulls(df):
    '''
    Function to set a threshold and remove rows and columns with a higher percentage of nulls
    than this threshold.
    '''

    # Removing Nulls from Columns
    # sets thresh hold to 75 percent nulls, if more than %25 nulls it will be removed
    threshold = df.shape[0] * .50

    # remove columns with specified threshold
    df_prepped = df.dropna(axis=1, thresh=threshold)
    
    # Removing Nulls from Rows
    # sets thresh hold to 75 percent nulls, if more than %25 nulls it will be removed
    thresh_hold = df.shape[1] * .50

    # remove rows with specified threshold
    df_prepped = df.dropna(axis=0,thresh=thresh_hold)

    return df