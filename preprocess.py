import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("./data/processedData/merged_data.csv")

le = LabelEncoder()
data['Company'] = le.fit_transform(data['Company'])
data['City'] = le.fit_transform(data['City'])
data["Payment_Mode"] = le.fit_transform(data['Payment_Mode'])
data['Gender'] = le.fit_transform(data['Gender'])

data.drop(['Transaction ID', "Customer ID", 'Population', 'Users'], axis = 1, inplace = True)

years = []
months = []
dates = []
for i in range(len(data)):
    date, month, year = data['Date of Travel'][i].split('-')
    years.append(int(year))
    months.append(int(month))
    dates.append(int(date))

data['dates'] = dates
data['months'] = months

data.drop(['Date of Travel'], axis = 1, inplace = True)

data.to_csv("./data/processedData/preprocessed_data.csv", index=False)