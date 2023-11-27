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
    
(
 ggplot(boot_df, aes(x = "x")) +
 geom_histogram(color = "#154734", fill = "#FFB81C")
 )

#%%

class BootCI:
    def __init__(self, data = None, stat = "mean"):
        """Initializes the class"""
        self._stat = stat
        self._dat = data
        self._boot_stat = []
        self._ci_level = 0.95
        
    def run_sims(self, n):
        """Runs bootstrap simulations"""
        for i in range(n):
            boot_sample = self._dat.sample(len(self._dat), replace = True)
            
            if self._stat == "median":
                self._boot_stat.append(float(boot_sample.median()))
            elif self._stat == "mean":
                self._boot_stat.append(float(boot_sample.mean()))
            elif self._stat == "std dev":
                self._boot_stat.append(float(boot_sample.std())) 
            else:
                raise TypeError("Invalid statistic name")
                
    def clear_list(self):
        """Resets the boot_stat list"""
        self._boot_stat = []
        
#%%

dat = pd.read_csv("2017_Fuel_Economy_Data.csv")
dat = dat["Combined Mileage (mpg)"]

test1 = BootCI(dat)  
test1.run_sims(10000)   
test1.clear_list()  

test2 = BootCI(dat, "median")
test2.run_sims(10000)
test2.run_sims(5000)
test2.clear_list()

test3 = BootCI(dat, "std dev")
test3.run_sims(10000)
test3.clear_list()


        
























