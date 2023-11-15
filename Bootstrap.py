"""
Created on Wed Oct 18 15:03:07 2023

@author: Ryan
"""

from plotnine import *
import pandas as pd
import os

os.chdir("C:/Users/Ryan/OneDrive/Desktop/STA 2450")

dat = pd.read_csv("2017_Fuel_Economy_Data.csv")
dat = dat["Combined Mileage (mpg)"]
n = len(dat)
n_boot = 10000

stat = "mean"

boot_stat = []
for i in range(n_boot):
    boot_sample = dat.sample(n, replace = True)
    
    if stat == "median":
        boot_stat.append(float(boot_sample.median()))
    elif stat == "mean":
        boot_stat.append(float(boot_sample.mean()))
    elif stat == "std dev":
        boot_stat.append(float(boot_sample.std())) 
    else:
        raise TypeError("Invalid statistic name")
      
boot_df = pd.DataFrame({"x": boot_stat})
    
+(
 ggplot(boot_df, aes(x = "x")) +
 geom_histogram(color = "#154734", fill = "#FFB81C")
 )

#%%

class BootCI:
    def __init__(self):
        """Initializes the class"""
        self._stat = "mean"
        self._dat = None
        self._n_boot = 0
        self._boot_stat = None
        self._ci_level = 0.95
        
    
        
























