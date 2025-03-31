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

### Extracting the loans data from the cloud
Initaly the ```csv_check(self, csv_name)``` method checks if the loads data *.csv is present if not it downloads it from the database, infuture this could be devloped to check for updates. Code was written to connect to cloud AWS hosted database with a python scipt using the psycopg2/sqlalchemy libraries, from the database the "loans_payments" table is extracted to a df then saved as a *csv file. 

 ![Alt](/init_img.png "__init_ magic method")

### Examining data
The ```loans_payment.csv``` is loaded to a data frame.

## Installation instructions

### Setting up conda environment
We set up the conda encironment, I am including instruction of how I do this, later we may want to clone the envirnomant, ```conda create -n loans_in_fin  python=3.10```, we activate our conda environment ```conda activate loans_in_fin```. Next we install packages we will need.

``` conda -c install pandas numpy psycopg2 sqlalchemy pyyaml```

## Usage instructions

## File structure of the project

## License information

This is availible through a GNU General Public License, version 3.
