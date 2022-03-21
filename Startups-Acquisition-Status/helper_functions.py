from typing import final
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

csv_file_path = 'CleanedData.csv'

def read_dataframe():
    return pd.read_csv(csv_file_path, index_col=False)

def extend_user_input(userinput):
    ex_user_input = []
    category_country_list = []
    df = read_dataframe()
    df_columns = df.columns
    #Getting columns names encoded for category and country columns
    for col in df_columns:
        if col.startswith(('cat', 'coun')):
            category_country_list.append(col)

    #Setting the gain of user input with one and remaining columns with zero
    category, country = userinput[-2:]
    category = 'category_code_' + str(category)
    country  = 'country_code_' + str(country)

    for col in category_country_list:
        if col == category or col == country:
            ex_user_input.append(1)
        else:
            ex_user_input.append(0)

    return ex_user_input

def concat_final_user_input(l1, l2):
    returned_list = []
    for ele in l1:
        returned_list.append(ele)
    for ele in l2:
        returned_list.append(ele)
    return np.asarray(returned_list)

def user_input_preprocessing(input):
    scaler = StandardScaler()
    return scaler.fit_transform(input)
    
def modling_func(user_input):
    #adding the part which is OneHotEncoded
    extended_user_input = extend_user_input(user_input)
    extended_user_input = np.asarray(extended_user_input)
    
    # load, no need to initialize the models again
    loaded_model = joblib.load("voting_model_weights.joblib")

    #removing category/country code from user input (don't need anymore)
    user_input = user_input[:-2]
    user_input_reshaped = user_input.reshape(-1, 1)

    #applying standard scaler on user input
    user_input_scaled = user_input_preprocessing(user_input_reshaped)
    #convert from array of array to array of floats
    user_input_scaled = user_input_scaled.astype(float)

    #Concatinaing the user input with the extended input for encoding features
    final_user = concat_final_user_input(user_input_scaled, extended_user_input)

    #Predicting user input
    predictions = loaded_model.predict(final_user.reshape(1, 35))
    return predictions