import matplotlib.pyplot as plt
import numpy as np
import warnings
import math
import pandas as pd

def clean_ZAlizadehsani():
    '''
    data cleaning for Z-Alizadeh Sani data set (Z-Alizadeh sani dataset.xlsx)
    convert data frame with 6 common attributes to numpy array from Iran data set
    df: the data frame read from file
    return matrix with 5 values and a label matrix
    
    INPUTS
    :param extra: whether or not to add extra data fields
    :type extra: bool
    
    OUTPUTS
    :param y: the output attributes data
    :type y: a numpy data array
    :param indicator: the output indicator
    :type indicator: a numpy data array
    '''
    df = pd.read_excel('Z-Alizadeh sani dataset.xlsx')
    
    # first matrix for 5 values
    dff1 = df[['Sex','Age','Current Smoker', 'BP', 'FBS']].replace('Male', 1)
    dff2 = dff1.replace('Fmale', 0)
    y = dff2.values.transpose()

    # second matrix with labels
    df1 = df['Cath'].replace('Cad', 1)
    df2 = df1.replace('Normal', 0)
    indicator = df2.values.transpose()
    
    return y, indicator