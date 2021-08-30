
import pandas as pd
import numpy as np
import os
from env import host, user, password



def get_db_url(url="employees"):
    url = f'mysql+pymysql://{user}:{password}@{host}/{url}'
    return url
    
def new_telco_data():
    '''This function reads the telco data from the Codeup db into a df,
    write it to a csv file, and returns the df. '''
    # Create SQL query.
    sql_query = """ SELECT *
                    FROM customers
                    JOIN contract_types
	                    ON customers.contract_type_id = contract_types.contract_type_id
                    JOIN internet_service_types
                        ON customers.internet_service_type_id = internet_service_types.internet_service_type_id
                    JOIN payment_types
                        ON customers.payment_type_id = payment_types.payment_type_id"""
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_db_url('telco_churn'))
    
    return df

def get_telco_data():
    '''
    This function reads in titanic data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('telco_churn.csv'):
        
        # If csv file exists, read in data from csv file.
        df = pd.read_csv('telco_churn.csv', index_col=0)     
    else:  
        # Read fresh data from db into a DataFrame.
        df = new_telco_data()
        
        # Write DataFrame to a csv file.
        df.to_csv('telco_churn.csv')   
    return df

def get_data_dictionary(df):
    
    d_list = ['Identification number for customer', 
                    'Customer gender, male or female', 
                    'Yes or No, is the customer a senior citizen', 
                    'Yes or No, does the customer customer has a parter', 
                    'Number of dependents a customer has', 
                    'Number of months a customer has been with the company', 
                    'Phone Service plan, Yes or No', 
                    'Multiple lines, Yes or No', 
                    '1, 2, 3', 
                    'Yes, no, or no internet service',
                    'Yes, no, or no internet service', 
                    'Yes, no, or no internet service',
                    'Yes, no, or no internet service', 
                    'Yes, no, or no internet service',
                    'Yes, no, or no internet service',
                    '1, 2, 3', 
                    'Yes or no, whether or not the customer uses paperless billing', 
                    '1, 2, 3, 4',
                    'Monthly charges the customer pays',
                    'Total charges the customer has paid',
                    'Yes or no, whether or not the customer has churned',
                    '1, 2, 3',
                    'Month-to-month, One year, Two year',
                    '1, 2, 3',
                    'DSL, Fiber Optic, or None',
                    '1, 2, 3, 4',
                    'Electronic check, mailed check, bank transfer, or credit card payment',
                    ]
    data_dictionary = pd.DataFrame([{'Feature': col,
         'Datatype': f'{df[col].count()} non-null: {df[col].dtype}'} for col in df.columns])
    
    describe = pd.Series(d_list)
    df = pd.concat([data_dictionary, describe.rename("Description")], axis = 1)
    return df.set_index("Feature")

def get_target(df):    
    df = get_data_dictionary(df)
    df= df.reset_index()
    df = df.rename(index = {20: 'Target'})
    return df.iloc[20]


