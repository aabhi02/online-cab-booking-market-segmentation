import pandas as pd

cab_data=pd.read_csv('./data/Cab_Data.csv')
transac=pd.read_csv('./data/Transaction_ID.csv')
cust_data=pd.read_csv('./data/Customer_ID.csv')

transac_cust=transac.merge(cust_data, on='Customer ID', how='left')
temp_data=cab_data.merge(transac_cust, on='Transaction ID', how='left')
city_data=pd.read_csv('./data/City.csv')
temp_data=temp_data.merge(city_data, on='City', how='left')

temp_data.to_csv('./data/processedData/merged_data.csv', index=False)