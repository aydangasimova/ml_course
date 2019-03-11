import pandas as pd
data = pd.read_csv('../data/adult.data.csv')

print(data.head())
print(data.columns)

#answer to q1
print(data.groupby(['sex']).size())

#answer to q2
print(data.groupby(['sex']).mean())

#answer to q3
print(data.groupby(['native-country'], native-country='Germany' ).size())
