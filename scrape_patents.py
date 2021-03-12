"""
Description:
Extract patent abstracts from the web and store on local 
machine in text files

Created By: Daniel Van Hoesen
Creation Date: 03/12/2021


Notes:
References:
"""

#################
### Imports
#################

import pypatent
import pandas as pd
import time


#################
### Functions
#################



#################
### Main
#################

if __name__ == "__main__":
    
    n = 20
    
    start = time.time()
    
    results = pypatent.Search("wine", results_limit=n).as_dataframe()
    
    for col in results.columns:
        print(col)
    
    end = time.time()
    print("Time for %s downloads: " %str(n), end - start)
    
    
    for i in range(len(results.abstract.values)):
        print("\n", results.abstract.values[i])
    
    
    
