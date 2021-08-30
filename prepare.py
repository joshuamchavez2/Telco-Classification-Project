from math import sqrt
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pydataset import data
import statistics
import acquire
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer
import warnings
warnings.filterwarnings("ignore")

def clean_telco(df):

    #df = acquire.get_telco_data() # grabbing the telco data
    df = df.drop_duplicates() # Dropping Duplicates
    df = df.drop(columns = ['customer_id']) # Don't need this column
    
    # If total charges are null, then remove the entire row 
    list_of_null_indexs = list(df[df.total_charges.str.contains(" ")].index)
    df = df.drop(list_of_null_indexs)
    
    # Convert total_charges from datatype object to float
    total_charges = df.total_charges.astype("float")
    df = df.drop(columns='total_charges')
    df = pd.concat([df, total_charges], axis = 1)
    
    # In the three lines below are mapping out the current values for what they actually represent.
    payment = df.payment_type_id.map({1: 'Electronic check', 2: 'Mailed check', 3:'Bank transfer', 4:'Credit card'})
    internet = df.internet_service_type_id.map({1: 'DSL', 2: 'Fiber optic', 3:'None'})
    contract = df.contract_type_id .map({1: 'Month-to-month', 2: 'One year', 3:'Two year'})
    senior = df.senior_citizen.map({1: "Yes", 0: "No"})
    
    # In the three lines below im adding each series to my dataframe and renaming the columns
    df = pd.concat([df, payment.rename("payment")], axis = 1)
    df = pd.concat([df, internet.rename("internet_service")], axis = 1)
    df = pd.concat([df, contract.rename("contract")], axis = 1)
    df = pd.concat([df, senior.rename("senior")], axis = 1)
    
    df = df.drop(columns=['payment_type_id', 'payment_type_id.1','contract_type_id', 'contract_type_id.1', 'payment_type' ,'internet_service_type','internet_service_type_id', 'internet_service_type_id.1']) # Dropping old and duplicate columns
    
    boolean = df.nunique()[df.nunique() <= 2].index # boolean is a list of columns who's values are either true/false or 1/0

    # In the line below, I am making dummies for all the boolean columns.  Dropping the first so I dont get two columns back
    boolean_dummy = pd.get_dummies(df[boolean], drop_first=[True, True, True, True, True, True, True])
    
    # Adding my encoded boolean_dummy DataFrame back to my original Data Frame
    df = pd.concat([df, boolean_dummy], axis = 1)

    # Dropping the none encoded columns
    df = df.drop(columns=boolean) 
    
    # In the line below, I am grabbing all the categorical columns(that are greater than 2) and saving the values into categ as a list
    categ = df.nunique()[(df.nunique() > 2) & (df.nunique() < 5)].index

    # Grabbing dummies, this time dont drop the first columns.
    categ_dummy = pd.get_dummies(df[categ]) # Grabbing dummies, this time dont drop the first columns.
    
    
    df = pd.concat([df, categ_dummy], axis = 1) # Adding my encoded categ_dummy DataFrame back to my original Data Frame
    df = df.drop(columns=categ)  # Dropping the none encoded columns
    
    df = df.rename(columns={'churn_Yes': 'churn'})
    return df

def split_telco_data(df):
    
    train, test = train_test_split(df, test_size = 0.2, random_state = 123, stratify = df.churn)
    train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train.churn)
    
    return train, validate, test

def prep_telco_data(df):
    """
    takes in a data from titanic database, cleans the data, splits the data
    in train validate test and imputes the missing values for embark_town. 
    Returns three dataframes train, validate and test.
    """
    df = clean_telco(df)
    train, validate, test = split_telco_data(df)
    #train, validate, test = impute_mode(train, validate, test) #nothing to impute no missing values
    return train, validate, test