import matplotlib.pyplot as plt
import numpy as np
import warnings
import math

def plot_bargraphs(x_data, y_data, data_ind, num_ranges=3):
    '''
    Plot bargraphs showing prevalence of heart disease as a function of a specified
    feature from a dataset. Also plots piecharts showing the demographics of those
    within each data range that have heart disease.
    
    INPUTS
    :param data: Numpy array with feature vectors from ONE dataset
    :type data: numpy.ndarray
    :param data: Numpy array with feature vectors from ONE dataset
    :type data: numpy.ndarray
    :param data_ind: index of data feature to be plotted from dataset
    :type data_ind: int
    :param num_ranges: Number of intervals to split data into. Equals number of bars in final bargraph
    :type num_ranges: int
    '''
    # Asserts
    assert isinstance(x_data,np.ndarray) # assert that x_data is a numpy array
    assert isinstance(y_data,np.ndarray) # assert that y_data is a numpy array
    assert isinstance(data_ind, int)     # assert data_ind is an int
    assert isinstance(num_ranges, int)   # assert num_ranges is an int
    
    m, n = x_data.shape
    #assert y_data.shape == (n,1) # assert y is an n by 1 vector
    
    # Determine what value to plot statistics for using vaue of data_ind
    # For all datasets:
    # value of data_ind      Feature value
    # 1                      Age (years)
    # 2                      Current Smoker (yes/no)
    # 3                      Blood Pressure (mmHg)
    # 4                      Blood sugar (mg/dL; for UCI: yes/no above 120 mg/dL)
    # For UCI datasets only
    # 5                      History of diabetes (yes/no)
    # for Framingham dataset only
    # 5                      Is diabetic (yes/no)
    # 6                      BMI (BMI value)
    # 
    # Only the above values are valid. Anything else throws an error
    is_bin_data = False
    value_name = ''
    x_label = ''
    units = ''
    
    if data_ind == 1: # Age
        value_name = 'Age'
        units = 'years'
    elif data_ind == 3: # Blood pressure
        value_name = 'Blood Pressure'
        units = 'mmHg'
    elif data_ind == 4: # Blood sugar
        value_name = 'Blood Sugar'
        units = 'mg/dL'
    elif data_ind == 6: # BMI
        value_name = 'BMI'
        units = 'BMI'
    # asssume all other cases are binary yes/no, force num_ranges to be 2
    elif data_ind == 2: # current smoker
        value_name = 'Current Smoking Habit'
        x_label = 'Current smoker?'
        is_bin_data = True
        num_ranges = 2
    elif data_ind == 5: # diabetic
        value_name = 'Diabetes'
        x_label = 'Is diabetic?'
        is_bin_data = True
        num_ranges = 2
    else:
        raise ValueError('Invalid data_ind')
    
    
    # Determine boundaries of ranges to catagorize patients
    min_val = min(x_data[data_ind,:])
    max_val = max(x_data[data_ind,:])
    ranges = []

    step = (max_val - min_val) / num_ranges
    prev_val = min_val
    for i in range(num_ranges):
        ranges.append( (prev_val, prev_val + step) )
        prev_val += step
    
    
    # Separate patients into the seperate ranges based on value specified (num_ranges)
    num_points = x_data.shape[1]
    range_data = [np.zeros((0,2))] * num_ranges

    for i in range(num_points):
        for rng_num in range(num_ranges):
            rng = ranges[rng_num]
            
            if i < (num_ranges - 1):
                if rng[0] <= x_data[data_ind,i] < rng[1]:
                    new_data = np.array([[ x_data[0, i], y_data[i] ]])
                    
                    range_data[rng_num] = np.append(range_data[rng_num], new_data, axis=0)
                    break
            else:
                if rng[0] <= x_data[data_ind,i] <= rng[1]:
                    new_data = np.array([[ x_data[0, i], y_data[i] ]])
            
                    range_data[rng_num] = np.append(range_data[rng_num], new_data, axis=0)
                    break
    
    
    # For each range, find percentage of those with heart disease within
    # - Everyone in that range (totalPerc)
    total_perc = []
    num_people = [] # Each elemenr will be a 3-tuple containing: (total number of people with heart disease, men with heart disease, women with heart disease)
    
    for i in range(num_ranges):
        male_ind = np.where(range_data[i][:,0] == 1)[0]
        female_ind = np.where(range_data[i][:,0] == 0)[0]
        
        total_num = range_data[i].shape[0]
        male_num = male_ind.shape[0]
        female_num = female_ind.shape[0]
        
        total_perc.append(100 * np.sum(range_data[i][:,1], axis=0) / total_num)
        #male_perc.append(np.sum(range_data[i][male_ind,1], axis=0) / male_num)
        #female_perc.append(np.sum(range_data[i][female_ind,1], axis=0) / female_num)
        
        num_people.append( (np.sum(range_data[i][:,1], axis=0), np.sum(range_data[i][male_ind,1], axis=0), np.sum(range_data[i][female_ind,1], axis=0)) ) 
    
    
    #### Set up plots
    
    ## plot bar graph
    # Code for plotting graph based on example from this site:
    # https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
    
    # Create range labels for graph
    labels = []
    
    for i in range(num_ranges):
        labels.append(('%.2f' % ranges[i][0]) + ' - ' + ('%.2f' % ranges[i][1]))
    # If data_ind specifies a binary value, change "range" labels to reflect "yes" and "no" groups
    if ranges == [(0,0.5),(0.5,1)]:
        labels = ['No','Yes']
    
    x= np.arange(len(labels))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(7,5))
    ax.set_ylim(0,100)
    rectsTotal = ax.bar(x, total_perc, width)
    
    ## add titles n' stuff
    ax.set_ylabel('Percentage of people in range with heart disease')
    if is_bin_data: ax.set_xlabel(x_label)
    else: ax.set_xlabel('Ranges (in ' + units + ')')
    ax.set_title('Prevalence of Heart Disease As a Function of ' + value_name)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    
    # print values over bars
    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        #for rect in rects:
        for i in range(len(rects)):
            rect = rects[i]
            height = rect.get_height()
            ax.annotate('{}'.format(('%.2f' % (height)) + '% of\n' + ('%d' % range_data[i].shape[0]) + ' people' ),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
    
    autolabel(rectsTotal)
    
    fig.tight_layout()
    
    plt.show()
    
    
    ## plot pie charts
    # code source: https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_demo2.html
    for i in range(num_ranges):
        bar_labels = 'Men (' + ('%d' % num_people[i][1]) + ' people)', 'Women (' + ('%d' % num_people[i][2]) + ' people)'
        fracs = [num_people[i][1], num_people[i][2]]

        # Make figure and axes
        fig, ax = plt.subplots()

    
        # A standard pie plot
        ax.pie(fracs, labels=bar_labels, autopct='%1.1f%%', shadow=True)
        if is_bin_data:
            has_feature = (ranges[i][-1] > 0.5)
            if has_feature:
                ax.set_title('Gender Makeup of Those With Heart Disease With\n' + value_name)
            else:
                ax.set_title('Gender Makeup of Those With Heart Disease Without\n' + value_name)
        else: ax.set_title('Gender Makeup of Those With Heart Disease With\n' + value_name + 
                           ' in Range ' + labels[i] + ' ' + units)
        plt.show()
    
    return