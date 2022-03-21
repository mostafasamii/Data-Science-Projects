ex_user_input = []
category_country_list = []
df = pd.read_dataframe('CleanedData.csv', index_col=False)
df_columns = df.columns
#Getting columns names encoded for category and country columns
for col in df_columns:
    if col.startswith(('cat', 'coun')):
        category_country_list.append(col)

#Setting the gain of user input with one and remaining columns with zero
category, country = userinput[-2:]
for col in category_country_list:
    if col == category or col == country:
        ex_user_input.append(1)
    else:
        ex_user_input.append(0)

print(ex_user_input)
