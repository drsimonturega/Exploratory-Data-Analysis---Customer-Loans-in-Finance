# Plotter class to visualise insights from the data


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
import os
import pandas as pd
import plotly.express as px
import seaborn as sns
import statistics as st
from dat_frame_inf import DataFrameInfo
from statsmodels.graphics.gofplots import qqplot
from tabulate import tabulate



class Plotter:
    def __init__(self):
        #self.curr_df = curr_df
        print("init_Plotter")
        

    
    def compare_null_val(self, pre_df, post_df):
        """
        Provides percentage of na values

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        df_curr -- current df

        """
        # initialise class to use a method
        info_here = DataFrameInfo()
        # calculate % na
        percent_null = info_here.percent_na(pre_df)
        post_percent_null = info_here.percent_na(post_df)
        percent_null["post %_NULL"] = post_percent_null["%_NULL"]
        percent_null.rename({"data_col": "pre %_NULL"}, inplace=True)
        info_here.build_stat_tab(percent_null)             
        return 
    
    def grid_hist_kde_skew(self, curr_df, cont_lst):
        """
        Produces a grid plot of histograms with KDE

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        pre_df -- df prior to imputeing NULL values
        post_df -- df post imputeing NULL values

        """
        # this does not work ans could be tricky to get working
        categorical_features = [col for col in curr_df.columns if col not in cont_lst]
        sns.set(font_scale=0.7)
        f = pd.melt(curr_df, value_vars=cont_lst)
        g = sns.FacetGrid(f, col="variable",  col_wrap=3, sharex=False, sharey=False)
        g = g.map(sns.histplot, "value", label="Skewness: %.2f"%(curr_df.skew()), kde=True )

                   
        return 
    
    def grid_hist_kde(self, curr_df, cont_lst):
        """
        Produces a grid plot of histograms with KDE

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a df not string
        cont_lst -- list of columns of contiunous data

        """
        #categorical_features = [col for col in curr_df.columns if col not in cont_lst]
        sns.set(font_scale=0.7)
        f = pd.melt(curr_df, value_vars=cont_lst)
        g = sns.FacetGrid(f, col="variable",  col_wrap=3, sharex=False, sharey=False)
        g = g.map(sns.histplot, "value", kde=True )

               
        return  

    def categ_feat(self, curr_df, cont_lst):
        """
        Produces a grid plot of histograms with KDE

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a df not string
        cont_lst -- list of columns of contiunous data
        categorical_features -- list of columns of catagorical data

        """
        categorical_features = [col for col in curr_df.columns if col not in cont_lst]
        return categorical_features

    def count_categ_data(self, curr_df, cat_lst):
        """
        Produces a grid plot of histograms with KDE

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a df not string
        cat_lst -- list of columns of catagorical data
        """
        f = pd.melt(curr_df, value_vars=cat_lst)
        g = sns.FacetGrid(f, col='variable',  col_wrap=3, sharex=False, sharey=False)
        g = g.map(self.countplot, 'value')


    def countplot(self, x, **kwargs):
        """
        Preperation for multi count plot

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        x -- data column or list
        **kwargs -- **kwargs
        """
        sns.countplot(x=x)
        x=plt.xticks(rotation=90)
        

        
    
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
        # Indentify which columun I am investigating
        print(f'...\n {curr_col}')
        # produce a Quantile-Quantile plot
        qq_plot = qqplot(data , scale=1 ,line='q')
        plt.show()
        print(f'\n {curr_df[curr_col].describe()}\n')
        return
    
    def multi_q_q_plot(self, curr_df, col_lst):
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
        q_q_multi = [self.q_q_plot(curr_df, col) for col in  col_lst ]
        #print(q_q_multi)
        return
    
    def mat_hm_corr_plot(self, curr_df, plt_title):
        """
        Produces a Quantile-Quantile plot on df column

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a df not string
        """
        # thie may become duplicated and should be in Plotter class
        # collect data
        # Compute the correlation matrix
        corr = curr_df.corr()

        # Generate a mask for the upper triangle
        mask = np.zeros_like(corr, dtype=np.bool_)
        mask[np.triu_indices_from(mask)] = True

        # set thins up for plotting
        cmap = sns.diverging_palette(220, 10, as_cmap=True)

        # Draw the heatmap
        sns.heatmap(corr, mask=mask, 
                    square=True, linewidths=.5, annot=False, cmap=cmap)
        plt.yticks(rotation=0)
        plt.title(plt_title)
        plt.show()
        return
    
    

if __name__ == "__main__":
# database and data frame operations 
    plot_P = Plotter()
    