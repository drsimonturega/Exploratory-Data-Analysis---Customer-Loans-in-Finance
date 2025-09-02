# Exploratory-Data-Analysis---Customer-Loans-in-Finance
# multinational-retail-data-centralisation599

## Contents
* Introduction
* Code development
* Installation instructions
* Usage instructions
* File structure of the project
* License information


## Introduction
Currently I work for a large financial institution, where managing loans is a critical component of business operations.To ensure informed decisions are made about loan approvals and risk is efficiently managed, I have been tasked with developing a comprehensive understanding of the loan portfolio data. My job is to perform exploratory data analysis on the loan portfolio, using various statistical and data visualisation techniques to uncover patterns, relationships, and anomalies in the loan data. This information will enable the business to make more informed decisions about loan approvals, pricing, and risk management.

## Code development

### Seting up the environment
We set up a conda encironment, I am including instruction of how I do this, later we may want to clone the envirnomant, ```conda create -n loans_in_fin  python=3.10```, we activate our conda environment ```conda activate loans_in_fin```. Next we install packages we will need.

``` conda -c install pandas numpy psycopg2 sqlalchemy pyyaml```

### Extract the loans data
Extracting the loans data from the cloud. Initaly the ```csv_check(self, csv_name)``` method checks if the loads data *.csv is present if not it downloads it from the database, infuture this could be devloped to check for updates. Code was written to connect to cloud AWS hosted database with a python scipt using the psycopg2/sqlalchemy libraries, from the database the "loans_payments" table is extracted to a df then saved as a *csv file. 

 ![Alt](/init_img.png "__init_ magic method")

### Exploratory Data Analysis (EDA)
This milestone involves performing Exploratory Data Analysis (EDA) on the loans data. The main objective of the milestone is to gain a deeper understanding of the data and identify any patterns which might exist.

#### Check and convert columns to correct formats
Taking the data frame extracted from the database this is an initial round of Visualising column data types. Using the ```DataTransform()``` class it involves changing column types to a more usable format in columns where this can be anticipated and ensuring that columns are of the correct data type for example checking the categorical data column columns are categorical. This provides a dataframe that is ready for initial analysis. 

### 

#### Remove/impute missing values in the data

To clean the data  I create a class to get information from the DataFrame ```DataFrameInfo()```. This allows  the collection of discrptive statistics in columns of continous data and count distinct values in categorical columns. Get the shape of the DataFrame, count the NULL values in each column and sominitial visualisation ready for removing  or imputeing missing values. The descriptive statistics DataFrame outputs calculated in these methods can exported as a text in a "github" tabular format (eample in Table 1) or as a *.csv file. To deal with the Null values date columns with high NULL values that are  not needed are removed, in colums selected by visual analysis of discriptive statics have NUll vales replace by median or mean values.

Table 1, Descriptive statistics for our continuous             data coumns

| stat   |    term |   loan_amount |   funded_amount |   funded_amount_inv |   int_rate |   instalment |   collections_12_mths_ex_med |
|--------|---------|---------------|-----------------|---------------------|------------|--------------|------------------------------|
| median | 36      |      12000    |        20000    |             11300   |   19.52    |      347.15  |                   0          |
| st_dev | 10.7195 |       8082.12 |         8018.94 |              8099.4 |    4.39285 |      238.918 |                   0.0709895  |
| mean   | 42.6062 |      13333.1  |        13229.5  |             12952.6 |   13.5073  |      400.014 |                   0.00420819 |


#### Perform transformations on skewed columns
The skew of the coluns is idientifed ueing a meuli comun alanysis.  Applying the appropraite skew correcting fuction is achived using a Box-Cox or  Yeo-Johnson 
transformation to give a an improved skew magnitude to the columns. The column "last_payment_amount" apears to be biphasic, the skew does 
improve with a Yeo-Johnson correction so currently that will be apilled.

#### Dropping overly correlated columns
Column correllation was visualised using a heat map Method ```mat_hm_corr_plot()``` from the ```Plotter()``` class, figure below shows the heat map for column correlation before analysis.
 ![Alt](/corr_init.png "Heat map for column correlation before analysis")
 
The columns most highly correlated were emited using a thersh hold of correlation ratio of 0.95, coumns owith a correlation over this thesh hold were deopped. The correlation plot post analysis and column drop is given bellow.
 ![Alt](/corr_post.png "Heat map for column correlationpost analysis and column drop")




### Analysis and Visualisation
Now that the data has been cleaned, management would like to draw deeper insights from the data. You will dive deeper into the dataset to identify any patterns or trends not visible by your previous analysis. By gaining these deeper insights, management can make more informed decisions going forwards. The currency is not clearly deffined,  a place marker the currency Monero(XMR) 

#### Current state of the loans
The ```loans_payment.csv``` is loaded to a data frame. The current state of the loans is communicated as the percentage of the loans have been currently recovered compared to the total amount to be paid over the loans term including interest this is described using the histogram bellow. 

![Alt](/current_recovery_%.png "The current state of the loans")


#### Calculating loss
The company wants to check what percentage of loans have been a loss to the company, a plot of loan status is made to give an overview of staus of all loans in the data set.
![Alt](/current_recovery_%.png "Heat map for column correlationpost analysis and column drop")


#### Calculating projected loss
As a measure of projected loss I calculate the expected loss of the loans marked as **Charged Off**. I calculate the loss in revenue these loans would have generated for the company if they had finished their term as histogram of binned % losses and a value, a total of 91342.49648743XMR was lost on the charged off loans.


#### Possible loss

#### Indicators of loss


#### Final data analysis and visualisation


## Installation instructions

### Setting up conda environment
We set up a conda encironment, I am including instruction of how I do this, later we may want to clone the envirnomant, ```conda create -n loans_in_fin  python=3.10```, we activate our conda environment ```conda activate loans_in_fin```. Next we install packages we will need.

``` conda -c install pandas numpy psycopg2 sqlalchemy pyyaml```

## Usage instructions

The exploritory data analysis of the "lones in finance" data set, is run in a jupyter note book ```EDA.iypnb``` running python 10.6 with in a conda environment loans_in_fin. The note book is run on Microsofts VSCode on a laptop running ubuntu linux.

## File structure of the project

There are five python files, ```dat_tran.py```, ```datframe_inf.py```, ```datframe_tran.py```, ```plotter.py``` and ```db_utils.py``` that conatin the methods used in this propject. The each file contains a class of related methods for a specific part of the analysis the methods are run in a jupter note book ```EDA.iypnb```.

The ```db_utils.py``` contains a class ```RDSDatabaseConnector``` that has a method for extracting the lone data saveing it as a *.csv file opening it as a Pandas DataFrame. The ``dat_tran.py``` file contains the class DataTransform with methods for converting the types of columns and removing unwanted characters. A third pyrthon file ```datframe_inf_.py``` houses the class DataFrameInfo, this class contains methods for running some statistical analysis and saving the numerical out put as *.csv files when desired.  The python file ```datframe_tran.py``` contains the class DataFrameTransform with methods for cleaning data, imputing missing data, correcting skewed data and removing highly correlated columns from the data. The fith file ```plotter.py``` containd the Plotter class that has methods for plotting the data we explore in this project.

The exploritory data analysis is runs in my jupyter note book ```EDA.iypnb```.


## License information

This is availible through a GNU General Public License, version 3.
