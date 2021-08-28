
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