# Python script 'db_utils.py' here are the scripts to extract the data
# base needed for this analysis. This scrip contains the 
# 'RDSDatabaseConnector' class that hoses all the function needed to
# access the database.

class RDSDatabaseConnector:
    def __init__(self):
        self.hello = "hello world"
        
        
        
    def first_func(self):
        self.name = "paws"
        return
    def __str__(self):
        return self.hello
   


simon = RDSDatabaseConnector()
print(simon)