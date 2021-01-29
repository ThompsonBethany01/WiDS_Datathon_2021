# Project: Wids Datathon 2021 - Predicting Diabetes in ICU Patients
# File: Preprocessing.py
# Author: Bethany Thompson
# Date: January 2021
'''
Functions to prepare the cleaned df for modeling with data science best practices, such as splitting the data.
'''

# import needed to run functions 
import pandas as pd

############################################## Preprocssing Function ##############################################

def preprocess_data(df):

    return train, validate, test, train_scaled, validate_scaled, test_scaled
    
################################################# Helper Functions #################################################

# functions called within the main preprocess data function

def split_data(df):

    return train, validate, test

def scale_data(train, validate, test):

    return train_scaled, validate_scaled, test_scaled