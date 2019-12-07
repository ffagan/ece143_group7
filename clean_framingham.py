import matplotlib.pyplot as plt
import numpy as np
import warnings
import math
import pandas as pd

##Functions for data extraction and cleanup
def clean_framingham(extra=False):
    '''
    this function takes the framingham_1.csv file and extracts the necessary data 
    from this file, the output is two numpy arraies, the first one is the attributes 
    and the second one is the indicator of wether this patient has heart disease
    
    INPUTS
    :param extra: whether or not BMI and glucose data is included
    :type extra: bool
    
    OUTPUTS
    :param y: the output attributes data
    :type y: a numpy data array
    :param indicator: the output indicator
    :type indicator: a numpy data array
    '''
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        data = np.loadtxt(open("framingham_1.csv","rb"),delimiter=",",skiprows=1)
    #extracting the data needed
    y=data[:,[0,1,3,8,10,12,14,15]]
    row_num = np.shape(y)[0]
    #z is the list of row numbers that contains invalid data for one patient
    z=[]
    for i in range(row_num):
        if ((y[i,6]==0) or (y[i,5]==0)) and (i not in z):
            z.append(i)
    #deleting the patients with invalid data
    y = np.delete(y,z,axis=0)
    
    #indicator is the reulst of wether one patient has CAD
    indicator = y[:,7]
    indicator = indicator.T
    #dont have the BMI and glutcose data
    if extra == False:
        y = y[:,[0,1,2,4,6]]
        y = y.T
        #print(y)
        #print(indicator)
        return y,indicator
    #includes the BMI and glutcose data
    else:
        y = y[:,[0,1,2,4,6,3,5]]
        y=y.T
        #print(y)
        #print(indicator)
        return y,indicator