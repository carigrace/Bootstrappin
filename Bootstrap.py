"""
Created on Wed Oct 18 15:03:07 2023

@author: Ryan
"""

from plotnine import *
import pandas as pd
import numpy as np
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
from plotnine import *
import pandas as pd
import numpy as np
import os


class BootCI:
    def __init__(self, data = None, stat = "mean"):
        """
        Initializes the class BootCI

        Parameters
        ----------
        data : TYPE: Pandas data series that is required if you want to run
        simulations.
            DESCRIPTION. The default is None, but data is required if you want
            to run simulations.
            
        stat : TYPE: optional string  Options are "mean", "median", and "std dev"
            DESCRIPTION. The default is "mean".

        Returns
        -------
        None.

        """
        self._stat = stat
        self._dat = data
        self._boot_stat = []
        self._ci_level = 0.95
        
    def run_sims(self, n):
        """
        Runs the desired number of bootstrap simulations.

        Parameters
        ----------
        n : TYPE: Positive integer
            DESCRIPTION. : Number of bootstrap resampling simulations that will
            be ran

        Raises
        ------
        TypeError
            DESCRIPTION. : Error that will be raised if self._stat is not one
            of the three valid options, which are "mean", "median", and 
            "std dev"
            

        Returns
        -------
        None.

        """
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
        
    def change_stat(self, stat):
        """
        Changes the bootstrap statistic.

        Parameters
        ----------
        stat : TYPE: string.
                Options are "mean", "median", and "std dev" only
            DESCRIPTION. The type of bootstrap statistic

        Returns
        -------
        None.

        """
        self._stat = stat
        self.clear_list()
        
    def plot_bootstrap(self):
        """Plots a graph of the bootstrap distribution. If no simulations have
        been run, the plot will be empty."""
        
        boot_df = pd.DataFrame({"x": self._boot_stat})
        
        p = (
         ggplot(boot_df, aes(x = "x")) +
         geom_histogram(color = "#154734", fill = "#FFB81C")
         )
        
        return p
    
    def find_percentiles(self, conf_level = 0.95):
        """
        Finds the confidence interval at the given level.

        Parameters
        ----------
        conf_level : Float between 0 and 1, exclusive
            DESCRIPTION. The confidence level to be evaluated. The default is 
            0.95.

        Returns
        -------
        Returns the confidence limits in a list

        """
        ll = (1-conf_level)/2
        ul = (1+conf_level)/2
        if self._boot_stat == []:
            print("You have an empty list, please run a bootstrap.")
        else:
            n = np.percentile(self._boot_stat, [ll, ul])
            print(f"We are {conf_level*100} percent confident that the true \
{self._stat} is between {n[0]} and {n[1]}.")
            return n
        
#%%

## Using the class

dat = pd.read_csv("2017_Fuel_Economy_Data.csv")
dat = dat["Combined Mileage (mpg)"]

test1 = BootCI(dat)  
test1.run_sims(10000)  
test1.change_stat("std dev")
test1.run_sims(10000)
test1.plot_bootstrap()
test1.find_percentiles(0.98)
ci = test1.find_percentiles()
test1.clear_list()
test1.find_percentiles()


test2 = BootCI(dat, "median")
test2.run_sims(10000)
test2.run_sims(5000)
test2.clear_list()

test3 = BootCI(dat, "std dev")
test3.run_sims(10000)
test3.clear_list()


          
























