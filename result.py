import pandas as pd

region_name = input("Ievadiet reģiona nosaukumu: ")

description_file = "description.xlsx"
description_data = pd.read_excel(description_file, sheet_name="LookupAREA")

region_code = description_data.loc[description_data['Description'] == region_name, 'Area']

if region_code.empty:
    print(0) 
else:
    region_code = region_code.values[0] 

    data_file = "data.csv"
    data = pd.read_csv(data_file)

    geo_count_sum = data.loc[data['Area'] == region_code, 'geo_count'].sum()

    print(int(geo_count_sum)) 
