# DataTransformation class addresses columns which you think should be
# converted into a different format
import numpy as np
import os
import pandas as pd

class DataTransform:
    def __init__(self):
        #self.curr_df = curr_df
        print("init_")
        
    
    def pd_object_to_date(self, curr_df, inv_cols):
        """
        Converts columns with type pd object to datetime

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a ddf not string
        inv_cols -- list of columns for investigation 
        """
        # converting dates think format
        for c_col in inv_cols:
            curr_df[c_col] = pd.to_datetime(curr_df[c_col], errors='coerce').dt.strftime('%Y-%m')
        return curr_df
    
    def mixed_col_to_num(self, curr_df, inv_cols):
        """
        Converts columns that are strings to floats

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a ddf not string
        inv_cols -- list of columns for investigation
        """
        for c_col in inv_cols:
            curr_df[c_col] = curr_df[c_col].astype(str)
            curr_df[c_col] = curr_df[c_col].fillna(0)
            curr_df[c_col] = curr_df[c_col].astype(np.float64)
            #print(f'{type(curr_df[c_col])}')
        return curr_df
    
    def unwanted_char_removal_int(self, curr_df, inv_cols):
        """
        Removes unwanted characters from columns

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a ddf not string
        inv_cols -- list of columns for investigation
        """
        try:
            for c_col in inv_cols:
                #removes charaters given in regex can be changed here currently
                curr_df[c_col] = curr_df[c_col].str.replace(r'("|<|years|year|\+|months|")', '', regex=True)
        except AttributeError:
            print(f'Possible one of your columns is not type string \
            or this has prevoysly been run on these columns')
        return curr_df

    def change_to_cat(self, curr_df, inv_cols):
        """
        Changes columns in a list to catagroical

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        curr_df -- current df as a ddf not string
        inv_cols -- list of columns for investigation
        """
        for c_col in inv_cols:
                #removes charaters given in regex can be changed here currently
                curr_df[c_col] = curr_df[c_col].astype("category")
        return curr_df
     
    


    
if __name__ == "__main__":
    # database and data frame operations 
    dat_t = DataTransform()
    