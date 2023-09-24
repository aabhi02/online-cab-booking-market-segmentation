import pandas as pd

data = pd.read_csv("./data/UberDataset.csv")
data['PURPOSE'].fillna("NOT", inplace=True)
data['START_DATE'] = pd.to_datetime(data['START_DATE'],
                                       errors='coerce')
data['END_DATE'] = pd.to_datetime(data['END_DATE'],
                                     errors='coerce')
 
data['date'] = pd.DatetimeIndex(data['START_DATE']).date
data['time'] = pd.DatetimeIndex(data['START_DATE']).hour

data['day-night'] = pd.cut(x=data['time'],
                              bins = [0,10,15,19,24],
                              labels = ['Morning','Afternoon','Evening','Night'])
data.dropna(inplace=True)
data.drop_duplicates(inplace=True)

obj = (data.dtypes == 'object')
object_cols = list(obj[obj].index)

unique_values = {}
for col in object_cols:
  unique_values[col] = data[col].unique().size
data['DAY'] = data.START_DATE.dt.weekday
day_label = {
	0: 'Mon', 1: 'Tues', 2: 'Wed', 3: 'Thus', 4: 'Fri', 5: 'Sat', 6: 'Sun'
}
data['DAY'] = data['DAY'].map(day_label)
data.to_csv('./data/preprocessedData/preprocessedData.csv')