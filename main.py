##Print the data frame. 
import pandas as pd   
df = pd.read_csv('c:/projects of python/iris project/iris.csv')
print("Full DataFrame:")
print(df)

##Display top 5 rows.
import pandas as pd
df = pd.read_csv('c:/projects of python/iris project/iris.csv')
print(df.head())

##Compute statistical analysis on the data frame. 
import pandas as pd

df = pd.read_csv('c:/projects of python/iris project/iris.csv')

print("First five rows of the dataset:")
print(df.head())

print("\nStatistical analysis of the dataset:")
print(df.describe())

print("\nCount of samples for each species:")
print(df['species'].value_counts())

print("\nCorrelation matrix:")
print(df.corr())

print("\nData frame info:")
print(df.info())

print("\nCheck for missing values:")
print(df.isnull().sum())




