import numpy as np
import pandas as pd
import joblib
np.random.seed(0)
from helper_functions import *

def reverse_target_encoding(val):
    dic = {1: 'operating',
           2: 'acquired', 
           3: 'closed',
           4: 'ipo'}
    return dic[val]

def startup_prediction(user_input):
    #Get user predictions
    vot_predictions = modling_func(user_input=user_input)
    vot_predictions_list= list(vot_predictions)
    max_value = max(vot_predictions_list)
    index = vot_predictions_list.index(max_value) #index of max prediction value
    # reverse the target value to its original values "operating, closed, acquired, ipo".
    return reverse_target_encoding(max_value)