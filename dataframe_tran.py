# DataFrameTransform class to perform EDA transformations on your data

import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
import matplotlib.style as style
import os
import pandas as pd
import plotly.express as px
import seaborn as sns
import statistics as st
from scipy.stats import normaltest
from scipy import stats
from statsmodels.graphics.gofplots import qqplot
from tabulate import tabulate



class DataFrameTransform:
    def __init__(self):
        #self.curr_df = curr_df
        print("init_")
        
    def drop_col(self, curr_df, inv_col):
        """
        Provides statistics  for catagorical data columns from a
        df, presenting them as a table and saving as 'catog_stats.csv'

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        df_curr -- current df
        inv_cols -- list of columns for investigation
        """
        curr_df = curr_df.drop(columns = inv_col, axis=1, inplace=True)
        return curr_df

    def impute_df_col(self, curr_df, median_cols, mean_cols):
        """
        Converts columns with type pd object to datetime

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a df not string
        new_df -- name of new df 
        median_cols -- list containing columns that will be replaced with
        the median of the column
        mean_cols -- list containing columns that will be replaced with
        the mean of the column
        """
        #make new data frame
        new_df = curr_df.copy(deep=True)        
        # inputeing cols thats will replace NULL values with the median
        for column in median_cols:
            new_df[column] = new_df[column].fillna(new_df[column].median())
        # inputeing cols thats will be replace NULLL values with the median
        for column in mean_cols:
            new_df[column] = new_df[column].fillna(new_df[column].mean())
        self.inpute_dates(new_df)
        return new_df
    
    def inpute_dates(self, curr_df):
        """
        Converts columns with type pd object to datetime

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a df not string
        """
        # inputeing date cols thats will replace NULL values with the a
        # point of reference date 
        # "lastpayment" replaced with "issue date" 
        curr_df["last_payment_date"] = curr_df["last_payment_date"].fillna(curr_df["issue_date"])
        # "next_payment" replaced with "last_payment"
        curr_df["next_payment_date"] = curr_df["next_payment_date"].fillna(curr_df["last_payment_date"])
        # "next_payment" replaced with "last_payment"
        curr_df["last_credit_pull_date"] = curr_df["last_credit_pull_date"].fillna(curr_df["issue_date"])
        return curr_df

        
        

                

        



        
        return 
    
    def K_2_Test(self, curr_df, curr_col):
        """
        Runs a D’Agostino’s K^2 Test on df column

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a df not string
        curr_coll -- single column of interest
        """
        # collect data
        data = curr_df[curr_col]
        # run D’Agostino’s K^2 Test
        stat, p = normaltest(data, nan_policy='omit')
        print('Statistics=%.1f, p=%.3f' % (stat, p))
        curr_df[curr_col].hist(bins=40)
        return p
    
    def q_q_plot(self, curr_df, curr_col):
        """
        Produces a Quantile-Quantile plot on df column

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a df not string
        curr_coll -- single column of interest
        """
        # thie may become duplicated and should be in Plotter class
        # collect data
        data = curr_df[curr_col]
        # produce a Quantile-Quantile plot
        qq_plot = qqplot(data , scale=1 ,line='q')
        pyplot.show()
        return
    
    def drop_rows_con(self, curr_df, curr_col, curr_val):
        """
        Drops columnsS

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a df not string
        curr_coll -- single column of interest
        """
        curr_df = curr_df.drop(curr_df[curr_df[curr_col] == curr_val].index)
        # index is wonky...
        #curr_df = curr_df.reset_index()
        #curr_df = curr_df.drop(curr_df.columns[0], axis=1, inplace=True)
        return curr_df
    
    def hist_kde_skew(self, data_lst):
        """
        Performs a log transformation on a column

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        data_lst -- data as a list
        """
        #print(f'...\n {curr_col}\n')
        t1=sns.histplot(data_lst,label="Skewness: %.2f"%(data_lst.skew()), kde=True )
        t1.legend()
        qq_plot = qqplot(data_lst , scale=1 ,line='q', fit=True)
        plt.show()
        return
    
    def log_transform(self, curr_df, curr_col):
        """
        Performs a log transformation on a column

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a df not string
        curr_coll -- single column of interest
        """
        print(f'...\n {curr_col}\n')
        self.hist_kde_skew(curr_df[curr_col])
        log_col = curr_df[curr_col].map(lambda i: np.log(i) if i > 0 else 0)
        self.hist_kde_skew(log_col)
        return

    def box_cox_transform(self, curr_df, curr_col):
        """
        Performs a Box Cox transformation on a column, only for 
        positive values provides useful plots and skew values

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a df not string
        curr_coll -- single column of interest
        """
        print(f'...\n {curr_col}\n')
        self.hist_kde_skew(curr_df[curr_col])
        boxcox_population = curr_df[curr_col]
        boxcox_population= stats.boxcox(boxcox_population)
        boxcox_population= pd.Series(boxcox_population[0])
        self.hist_kde_skew(boxcox_population)
        return

    def yeo_johnson_transform(self, curr_df, curr_col):
        """
        Performs a Yeo Johnson transformation on a column, for 
        positive and negative values provides useful plots and skew

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a df not string
        curr_coll -- single column of interest
        """
        print(f'...\n {curr_col}\n')
        self.hist_kde_skew(curr_df[curr_col])
        yeojohnson_population = curr_df[curr_col]
        yeojohnson_population = stats.yeojohnson(yeojohnson_population)
        yeojohnson_population= pd.Series(yeojohnson_population[0])
        self.hist_kde_skew(yeojohnson_population)
        return

    def multi_box_cox_transform(self, curr_df, col_lst):
        """
        Performs a Box Cox transformation on a a list of columns, only for 
        positive values provides useful plots and skew values

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a df not string
        col_lst -- list of columns for transformation
        """
        #print(f'...\n {curr_col}\n')
        #self.hist_kde_skew(curr_df[curr_col])
        #curr_df[col] = [curr_df[col] for col in curr_df.columns pd.Series((stats.boxcox(curr_df[col]))[0])]
        for col in col_lst:
            print(f'{col}')
            boxcox_population = curr_df[col]
            boxcox_population= stats.boxcox(boxcox_population)
            curr_df[col] = pd.Series(boxcox_population[0])
        # do I need this?
        pd.options.display.max_columns = None
        print(f'{curr_df.head()}')
        #self.hist_kde_skew(boxcox_population)
        return

    def multi_yeo_johnson_transform(self, curr_df, col_lst):
        """
        Performs a Yeo Johnson transformation on a list of columns, 
        for positive and negative values no plots

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a df not string
        col_lst -- list of columns for transformation
        """
        #print(f'...\n {curr_col}\n')
        #self.hist_kde_skew(curr_df[curr_col])
        #curr_df[col] = [curr_df[col] for col in curr_df.columns pd.Series((stats.yeojohnson(curr_df[col]))[0])]
        for col in col_lst:
            print(f'{col}')
            yeojohnson_population = curr_df[col]
            yeojohnson_population= stats.yeojohnson(yeojohnson_population)
            curr_df[col] = pd.Series(yeojohnson_population[0])
        # do I need this?
        pd.options.display.max_columns = None
        print(f'{curr_df.head()}')
        #self.hist_kde_skew(boxcox_population)
        return

    def rm_zero_val_outlier(self, curr_df, col_lst):
        """
        Removes rows where col vales are zero

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a df not string
        col_lst -- list of columns for investigation
        """
        #[curr_df[col] for col in col_lst curr_df.drop(curr_df[curr_df[col] == 0].index, inplace = True)]
        for col in col_lst:
            curr_df.drop(curr_df[curr_df[col] == 0].index, inplace = True)
        return curr_df

    def rm_max_val_outlier(self, curr_df, col_lst):
        """
        Removes rows where col vales are zero

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a df not string
        col_lst -- list of columns for investigation
        """
        #[curr_df[col] for col in col_lst curr_df.drop(curr_df[curr_df[col] == 0].index, inplace = True)]
        for col in col_lst:
            col_max = curr_df[col].max()
            print(f'{col} max is {col_max}')
            print(f' df length = {len(curr_df)}')
            curr_df.drop(curr_df[curr_df[col] == col_max].index, inplace = True)
            print(f' df length = {len(curr_df)}')
        return curr_df

    def sel_corr_cols(self, curr_df, cut_off):
        """
        Removes columns where correlation with other columns is too high

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a df not string
        cut_off -- selected correlation value for removing a column
        """
        df = curr_df.corr()
        corr_lst = list()
        for col in list(df):
            df = curr_df.corr()
            df = df.loc[df[col] >= cut_off ]
            t_lst = list(df.index.values)
            t_lst.pop(0)
            corr_lst= corr_lst + t_lst
            #print(corr_lst)
        corr_lst = set(corr_lst)
        print(corr_lst)
        return corr_lst
    

if __name__ == "__main__":
    # database and data frame operations 
    dat_t = DataFrameTransform()
    