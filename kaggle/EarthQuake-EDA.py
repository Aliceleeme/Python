
# written by Alice Lee
# Goal; Attending the kaggle competition and studying the python codes to conduct ML projects 
# https://www.kaggle.com/c/LANL-Earthquake-Prediction
## references: https://www.kaggle.com/artgor/seismic-data-eda-and-baseline
##           : 

# libraries 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

# read the data
train = pd.read_csv('../input/train.csv', dtype={'acoustic_data': np.int16, 'time_to_failure': np.float32})

train.head()
