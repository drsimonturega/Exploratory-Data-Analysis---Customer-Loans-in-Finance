# DataTransformation class addresses columns which you think should be
# converted into a different format
#import numpy as np
import os
#import pandas as pd

class DataTransform:
    def __init__(self,csv_name):
        self.csv_name = csv_name

    def col_x_conv(self):
        """
        """
        print(f'check {self.csv_name}')
        return
        
if __name__ == "__main__":
    # database and data frame operations 
    dat_t = DataTransform("loan_payments")
    print(dat_t.col_x_conv())