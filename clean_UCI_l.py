import matplotlib.pyplot as plt
import numpy as np
import warnings
import math
import pandas as pd

def clean_UCI_l(extra=False):
    '''
    This function extracts the data and performs cleaning for the Long Beach data file
    (long-beach-va.data) from the UCI dataset
    
    INPUTS
    :param extra: whether or not diabetes data is included
    :type extra: bool
    
    OUTPUTS
    :param y: the output attributes data
    :type y: a numpy data array
    :param indicator: the output indicator
    :type indicator: a numpy data array
    '''
    f=open('long-beach-va.data')
    data=[]
    dat=[]

    # this block of code extracts the relevant data from the files and sort them
    for line in f.readlines():
        line = str(line)

        line = line.split()

        for i in line:
            if (i.startswith('-') and i[1:] or i).isdigit() or i.count('.')==1:
                i=float(i)

                dat.append(i)
            else:
                data.append(dat)
                dat=[]
    
    for x in data:
        if x[57]==0:
            pass
        else:
            x[57]=1
    num = len(data)
    
    
    # z is the index number of rows that contain invalid data and needs to be deleted
    z=[]
    for i in range(num):
        if (data[i][12]== -9 or data[i][9]==-9 or data[i][15]==-9 or data[i][15]==0) and (i not in z):
            z.append(i)
    
    # deleting the unusable data
    np_data = np.array(data)
    np_data =  np.delete(np_data,z,axis=0)
    
    # Extract feature: Sex, Age, Current Smoker, Blood pressure, blood sugar, heart disease or not 
    if extra == False: # will not include diabetes data
        y=np_data[:,[3,2,12,9,15,57]]
        y=y[:,[0,1,2,3,4]]
        indicator = np_data[:,57]
        y=y.T
        indicator=indicator.T
        #print('y is \n\n\n\n',y)
        #print('indi is \n\n\n\n\n\n',indicator)
        return y,indicator

    else: # will include diabetes data
        y=np_data[:,[3,2,12,9,15,57,16]]
        y=y[:,[0,1,2,3,4,6]]
        indicator = np_data[:,57]
        y = y.T
        indicator = indicator.T
        return y,indicator