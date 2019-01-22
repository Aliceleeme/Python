
# written by Alice Lee
# Goal; Attending the kaggle competition and studying the python codes to conduct ML projects 
# https://www.kaggle.com/c/LANL-Earthquake-Prediction



# libraries 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

# read the data
train = pd.read_csv('../input/train.csv', dtype={'acoustic_data': np.int16, 'time_to_failure': np.float32})

train.head()
