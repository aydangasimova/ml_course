import numpy as np
import pandas as pd
# we don't like warnings
# you can comment the following 2 lines if you'd like to
import warnings
warnings.filterwarnings('ignore')

#df = pd.read_csv('/home/aydan/Desktop/Courses/ml_course/data/telecom_churn.csv')
df = pd.read_csv('data/telecom_churn.csv')
print(df.head())

print(df.shape)
print(df.columns)
print(df.info())

df['Churn'] = df['Churn'].astype('int64')
df.describe()

df.describe(include=['object', 'bool'])
