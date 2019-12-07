import numpy as np
from matplotlib import pyplot as plt

def plot_dataset_demographics(data, dataset_name):
    '''
    Plot pie chart showing demographics of patients in dataset
    
    Pie chart code based of this example:
    https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts
    
    INPUTS
    :param data: Numpy array with feature vectors from ONE dataset
    :type data: numpy.ndarray
    :param name: Name of dataset
    :type name: str
    '''
    num_people = data.shape[1]
    
    male_ind = np.where(data[0,:] == 1)[0]
    female_ind = np.where(data[0,:] == 0)[0]
    
    num_males = len(male_ind)
    num_females = len(female_ind)
    
    
    bar_labels = 'Men (' + ('%d' % num_males) + ' people)', 'Women (' + ('%d' % num_females) + ' people)'
    fracs = [num_males, num_females]
    
    # Make figure and axes
    fig, ax = plt.subplots()
    
    # A standard pie plot
    ax.pie(fracs, labels=bar_labels, autopct='%1.1f%%', shadow=True)
    ax.set_title('Demographics of \n' + dataset_name + ' Dataset\n('
                 + ('%d' % num_people) + ' People)')
    
    plt.show()
    
    return num_people, num_males, num_females