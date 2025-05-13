# DataTransformation class addresses columns which you think should be
# converted into a different format
import numpy as np
import os
import pandas as pd
import plotly.express as px
import statistics as st
from tabulate import tabulate

class DataFrameInfo:
    def __init__(self):
        #self.curr_df = curr_df
        print("init_DataFrameInfo")
        

    
    def percent_na(self, curr_df, print=False):
        """
        Provides percentage of na values

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        df_current -- current df
        """
        #percent_null = pd.DataFrame
        percent_null = curr_df.isna().mean() * 100
        # calculate % na
        #print("percentage of missing values in each column:")
        #percent_null = percent_null.to_frame()
        percent_null = self.format_series(percent_null, "%_NULL", print)
        return percent_null
    
    def col_dtypes(self, curr_df):
        """
        Provides percentage of na values

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        df_current -- current df
        """
        #percent_null = pd.DataFrame
        curr_dtypes = curr_df.dtypes
        self.format_series(curr_dtypes, "dtype")
        return curr_dtypes
    
    def format_series(self, curr_series, curr_val, print=False):
        curr_series = curr_series.to_frame()
        curr_series['data_col'] = curr_series.index
        col = curr_series.pop('data_col')
        curr_series.insert(0, col.name, col)
        curr_series = curr_series.reset_index(drop=True)
        curr_series = curr_series.rename(columns={curr_series.columns[1]: curr_val})
        fun_file_name =  str(curr_series)
        if print == True:
            self.build_stat_tab( curr_series)
        return curr_series


    
    def desc_all_cols(self, curr_df):
        # Data types of all columns
        print(f'{curr_df.dtypes}')
        #print(f'{type(curr_df)}')
        return

    def desc_stats(self, curr_df ,index_lst ,inv_cols):
        """
        Provides descriptive statistics  for selected columns from a
        df, presenting them as a table and saving as 'stats_out.csv'

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        df_curr -- current df
        index_lst -- a list of stats values that form the index
        inv_cols -- list of columns for investigation
        """
        #build a df using the build_df_stats() function
        df_tab = self.build_df_stats(index_lst, inv_cols)
        # populate rows one column at a time
        for col_num in range(0,len(inv_cols)):
            df_tab.iloc[0, (col_num + 1)] = st.median(curr_df[inv_cols[col_num]])
            df_tab.iloc[1, (col_num + 1)] = np.std(curr_df[inv_cols[col_num]])
            df_tab.iloc[2, (col_num + 1)] = np.mean(curr_df[inv_cols[col_num]])
        # think about table numbering
        print("Table, Descriptive statistics for our continuous data coumns\n")
        self.build_stat_tab(df_tab)
        self.save_stat_tab(df_tab, 'desc_stats')
        return
    
    def stats_desc(self, curr_df, inv_cols, out_name):
        """
        Provides statistics  for catagorical data columns from a
        df, presenting them as a table and saving as 'catog_stats.csv'

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        df_curr -- current df
        inv_cols -- list of columns for investigation
        out_name -- name of output file
        """
        # build index column lst "index_lst"
        cat_desc = curr_df[inv_cols[0]].describe()
        stat_lst = cat_desc.index.values.tolist()
        df_tab = self.build_df_stats( stat_lst, inv_cols)
        for col_num in range(0,len(inv_cols)):
            cat_desc = curr_df[inv_cols[col_num]].describe()
            for stat_num in range(0,len(stat_lst)):
                df_tab.iloc[stat_num, (col_num + 1)] = cat_desc.iloc[stat_num]
        print("Table 2, Statistics for our data columns\n")
        self.build_stat_tab(df_tab)
        self.save_stat_tab(df_tab, out_name)
        return 
    
    def shape_df(self, curr_df):
        """
        Provides the shape of a date frame, returning the data 
        as a tuple.

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        df_curr -- current df
        """
        #returns shape of dataframe
        shape = curr_df.shape
        print(f'The df has {shape[1]} columns and {shape[0]} rows')
        return shape



    def build_df_stats(self, index_lst, inv_cols):
        """
        Provides a df for statistics from selected columns from a
        df, presenting them as a table and saving as 'stats_out.csv'

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        index_lst -- a list of stats values that form the index these go
        go in column 0 in new df to aid downstream use
        inv_cols -- list of columns for investigation these form 
        columns > 0 in the new df 
        """
        #build df
        df_tab = pd.DataFrame()
        # plot information, setup index with rows from index_lst
        df_tab.insert(0,"stat", range(0,len(index_lst)))
        # Line below is to stop a "dtype incompatible" warning and make
        #  the table apear more clear setting type as object
        df_tab["stat"] = df_tab["stat"].astype(object)
        for sat_calc in range(0,len(index_lst)):
            df_tab.iloc[sat_calc] = index_lst[sat_calc]
        # build columns for continuous data in list inv_cols
        for col_num in range(0,len(inv_cols)):
            # Type is set as None to stop a "dtype incompatible" 
            # warning and make the table apear more clear
            df_tab.insert((col_num + 1),inv_cols[col_num], None)
        return df_tab
    
    def build_stat_tab(self, out_df):
        """
        Provides a print out of a given df in a "github" tabular format
        and saves it as a *.csv

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        out_df -- output df for printing and saving
        """
        # design and print table
        stat_tab = tabulate(out_df, headers = out_df.columns,
            tablefmt = "github", showindex = False)
        print(stat_tab)
        return
    
    def save_stat_tab(self, out_df, out_name):
        try: #output results
            out_df.to_csv(f'{out_name}.csv',index=False)
        except PermissionError:
            print('The file we are trying to open may be open in another \
            program, please close and try again!')
        return 



    def column_info(self, curr_df ,single_col):
        """
        Provides statistics/info for a single selected columns from a
        df, presenting them as text output for developing further 
        data analysis code

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        df_curr -- current df
        single_col -- single columns investigation as a string
        """
        cat_desc = curr_df[single_col].describe()
        print(f'Description;\n{cat_desc}\n')
        print(f'Some info;\ndtype is {type(cat_desc)}')
        print(f'length is {len(cat_desc)}')
        print(f'first item in serise is {cat_desc.iloc[0]}\n')
        stat_lst = cat_desc.index.values.tolist()
        print(f'Acessesing the data;\nindex as a list "stat_lst",\n{stat_lst}')
        print(f'first item in the list is {stat_lst[0]}\n')
        return
    
    def object_info(self, inv_obj):
        """
        Provides statistics/info for a single selected columns from a
        df, presenting them as text output for developing further 
        data analysis code

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        inv_obj -- single columns investigation as a string
        """
        #cat_desc = curr_df[single_col].describe()
        print(f'Description;\n{inv_obj}\n')
        print(f'Some info;\ndtype is {type(inv_obj)}')
        print(f'length is {len(inv_obj)}')
        print(f'first item in serise is {inv_obj.iloc[0]}\n')
        stat_lst = inv_obj.index.values.tolist()
        print(f'Acessesing the data;\nindex as a list "stat_lst",\n{stat_lst}')
        print(f'first item in the list is {stat_lst[0]}\n')
        return
    
    def col_to_boxplot(self, curr_df, single_col):
        """
        Provides a boxplot from a single column from a dataframe

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        df_curr -- current df
        single_col -- single columns investigation as a string
        """
        fig = px.box(curr_df, y = single_col)
        fig.show()
        return
    
    def save_as_csv(self, curr_df, csv_name):
        """
        Saves the selected df as a *.csv file

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        df_curr -- current df to be saved
        csv_name -- name of *.csv file where database table is stored
        """
        try: #output results
            curr_df.to_csv(f'{csv_name}.csv',index=False)
        except PermissionError:
            print('The file we are trying to open may be open in another \
            program, please close and try again!')
        return
    
if __name__ == "__main__":
    # database and data frame operations 
    dat_F = DataFrameInfo()
    