# Python script 'db_utils.py' here are the scripts to extract the data
# base needed for this analysis. This scrip contains the 
# 'RDSDatabaseConnector' class that hoses all the function needed to
# access the database.
#imports tydy up
import numpy as np
import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
import yaml


class RDSDatabaseConnector:
    def __init__(self,csv_name):
        self.cred_file = "credentials.yaml"
        self.csv_name = csv_name
        self.csv_check(self.csv_name)
       
       
    def cred_load(self, cred_file):
        """
        load db credentials from a *.ymal file

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        cred_file -- *.ymal file with data base credentials 
        """
        # open cred file *.yaml, return a dictionary
        print(f'cred_load {cred_file}')
        with open(f'{cred_file}') as f:
            self.cred_dict = yaml.load(f, Loader=yaml.FullLoader)
        self.init_db_engine()
        return self.cred_dict
    
    def init_db_engine(self): 
        """
        read credentials, initialise and return an sqlalchemy db engine

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        """
        # connect to database using credientals loaded
        self.engine = create_engine(f"postgresql+psycopg2://{self.cred_dict['RDS_USER']}:{self.cred_dict['RDS_PASSWORD']}@{self.cred_dict['RDS_HOST']}:{self.cred_dict['RDS_PORT']}/{self.cred_dict['RDS_DATABASE']}")
        self.engine.execution_options(isolation_level='AUTOCOMMIT').connect()
        self.engine.connect()
        print(f'init_db_engine')
        return self.engine 
    
    def list_db_tables(self):
        """
        Lists data base tables

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        
        Returns database table names as a list
        """
        # List db tables so we select he correct one
        inspector = inspect(self.engine)
        self.tab_lst = inspector.get_table_names()
        print(f'here is {self.tab_lst}')
        return self.tab_lst
    
    def read_rds_table(self):  # can add external arguments
        """"
        Reads database table

        self -- variables that store information unique to each 
        object created from the class
        
        Returns a df conatining table extracted from db
        """
        tb_name = self.tab_lst[0]
        self.loan_payments = pd.read_sql_table(tb_name, self.engine)
                  
        return  self.loan_payments
    
    def csv_check(self, csv_name):
        """
        Check if the *.csv is in the folder and decided weather to
        download or not"

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        csv_name -- name of *.csv file where database table is stored

        """
        if os.path.isfile(f'{csv_name}.csv'):
            # load file
            print(f'loading file {csv_name}.csv')
            self.csv_load(csv_name)
        else:
            print(f'Conecting to db writing {self.csv_name}.csv and loading to df')
            self.download_db_table(self, csv_name)
        return
    
    def download_db_table(self, cred_file, csv_name):
        """
        Downloads db table stores it and loads it to df
        using existing functions 

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        cred_file -- *.ymal file with data base credentials 
        csv_name -- name of *.csv file where database table is stored

        Returns table in a df
        """
        self.cred_load(self.cred_file)
        self.list_db_tables()
        self.read_rds_table()
        self.csv_out()
        self.csv_load(csv_name)

    def csv_out(self):
        """
        Saves the extracted table as a *.csv file

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        csv_name -- name of *.csv file where database table is stored
        """
        try: #output results
            self.loan_payments.to_csv(f'{self.csv_name}.csv',index=False)
        except PermissionError:
            print('The file we are trying to open may be open in another \
            program, please close and try again!')
        return
    
    def csv_load(self, csv_name):
        """
        Loads the stored db table to a df

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        csv_name -- name of *.csv file where database table is stored

        Returns table in a df
        """
        # opening file from local directory
        self.df_loan = pd.DataFrame()
        try:
            self.df_loan = pd.read_csv(f'{csv_name}.csv')
        except PermissionError:
            print('The file we are trying to open may be open in another \
                program, please close and try again!')
        print(f'our df')
        print(self.df_loan.head())
        return self.df_loan
    
if __name__ == "__main__":
    # database and data frame operations 
    up_ld = RDSDatabaseConnector("loan_payments")
    
    