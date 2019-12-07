# Heart Disease Risk Analysis Using Data Science
Group 7's repo for ECE 143 final project, Fall 2019

# Datasets
- Framingham: http://archive.ics.uci.edu/ml/datasets/Heart+Disease
  - Dataset from Framingham, Massachuetts

- Z-Alizadeh Sani: https://archive.ics.uci.edu/ml/datasets/Z-Alizadeh+Sani#
  - data collected Dr Zahra Alizadeh Sani et al. from Iran University

- UCI Heart Disease dataset: https://www.kaggle.com/amanajmera1/framingham-heart-study-dataset
  - This is actually a collection of datasets from 4 different locations (two University Hospitals in Switzerland, Hungarian Institute of Cardiology in Budapest, and the V.A. Medical Centers in Long Beach and Cleveland). Of these datasets, the files we used were hungarian.data, long-beach-va.data, switzerland.data, and new.data.

The files for these datasets are included with this repo for convenience.

# File structure
- Functions for visualizations
  - plot_bargraphs.py: Plots bargraphs showing prevalence of heart disease as a function of a specified feature from a dataset. Also plots piecharts showing the demographics of those within each data range that have heart disease.
  - plot_dataset_demographics.py: Plots pie charts showing demographics of a given dataset
- Functions to clean data
  - clean_framingham.py: Framingham dataset
  - clean_ZAlizadehsani.py: cleans Z-Alizadeh Sani dataset
  - clean_UCI_h.py: cleans UCI Hungarian dataset
  - clean_UCI_l.py: cleans UCI Long Beach dataset
  - clean_UCI_n.py: cleans UCI "new" dataset
  - clean_UCI_s.py: cleans UCI Switzerland dataset
- Datasets
  - framingham_1.csv: original file for Framingham dataset
  - Z-Alizadeh sani dataset.xlsx: original file for Z-Alizadeh Sani dataset
  - hungarian.data: original file for UCI Hungarian dataset
  - long-beach-va.data: original file for UCI Long Beach dataset
  - new.data: original file for UCI "new" dataset
  - switzerland.data: original file for UCI Switzerland dataset
- Data Visualizations.ipynb: Jupyter Notebook where the above functions are used to produce the visualizations used in our presentation
- ECE_143_Final_Project_7_v1.pptx: Our group's presentation

# Dependencies
The following packages are used to run our code:
- matplotlib
- numpy
- pandas
- seaborn

The above modules can be installed using pip3
For example, installing matplotlib:
`pip3 install matplotlib`

# Running code
Please refer to the notebook `Data Visualizations.ipynb` for reference on how to use our functions.
