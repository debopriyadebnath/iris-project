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
print(df.describe())



##Display 10 random sample rows
import pandas as pd
df = pd.read_csv('c:/projects of python/iris project/iris.csv')
print(df.sample(10))

##Display the number of columns and names of the columns. 
import pandas as pd
df = pd.read_csv('c:/projects of python/iris project/iris.csv')
print("Number of columns:", len(df.columns))
print("Column names:", df.columns.tolist())

##Print the shape of the dataset. 
import pandas as pd

df = pd.read_csv('c:/projects of python/iris project/iris.csv')
print("Shape of the dataset:", df.shape)

##Fetch data from 5th row to 10th row. 
import pandas as pd

df = pd.read_csv('c:/projects of python/iris project/iris.csv')
print(df.iloc[4:10])


## Display data for two columns: petal. length and petal. width
import pandas as pd
df = pd.read_csv('c:/projects of python/iris project/iris.csv')
print(df[['petal.length', 'petal.width']])

##Counting the number of counts of each variety.
import pandas as pd
df = pd.read_csv('c:/projects of python/iris project/iris.csv')
print(df['variety'].value_counts())

## Display only those rows whose variety is Setosa.
import pandas as pd
df = pd.read_csv('c:/projects of python/iris project/iris.csv')
setosa_rows = df[df['variety'] == 'Setosa']
print(setosa_rows)


## Calculate the sum, mean and mode of a particular column (say petal. length).
import pandas as pd
df = pd.read_csv('c:/projects of python/iris project/iris.csv')
sum_petal_length = df['petal.length'].sum()
mean_petal_length = df['petal.length'].mean()
mode_petal_length = df['petal.length'].mode()[0]
print(sum_petal_length, mean_petal_length, mode_petal_length)


##Extract minimum and maximum value from a column (say petal. length). 
import pandas as pd
df = pd.read_csv('c:/projects of python/iris project/iris.csv')
min_petal_length = df['petal.length'].min()
max_petal_length = df['petal.length'].max()
print(min_petal_length, max_petal_length)


##Add a column (say total_value) to the dataset which will display the sum of the integer values of each row. 
import pandas as pd
df = pd.read_csv('c:/projects of python/iris project/iris.csv')
df['total_value'] = df.select_dtypes(include='number').sum(axis=1)
print(df.head())


## Rename the column name from variety to variety1 and reverse.
import pandas as pd
df = pd.read_csv('c:/projects of python/iris project/iris.csv')
df = df.rename(columns={'variety': 'variety1'})
print(df.head())
df = df.rename(columns={'variety1': 'variety'})
print(df.head())


##Remove the column 'total_value'. 
import pandas as pd
df = pd.read_csv('c:/projects of python/iris project/iris.csv')
if 'total_value' in df.columns:
    df = df.drop(columns=['total_value'])
print(df.head())


 ##Delete the first row of the data frame. 
import pandas as pd
df = pd.read_csv('c:/projects of python/iris project/iris.csv')
df = df.drop(index=0)
print(df.head())


##Delete the last row of the data frame. 
import pandas as pd
df = pd.read_csv('c:/projects of python/iris project/iris.csv')
df = df.drop(index=df.index[-1])
print(df.tail())


##Check if a value exists in data frame or not. 
import pandas as pd
df = pd.read_csv('c:/projects of python/iris project/iris.csv')
value_exists = df.isin(['Setosa']).any().any()
print(value_exists)


## Check if a value exists in a particular column or not.
import pandas as pd
df = pd.read_csv('c:/projects of python/iris project/iris.csv')
value_exists_in_column = df['variety'].isin(['Setosa']).any()
print(value_exists_in_column)


##Write the data frame to another csv file.
import pandas as pd
df = pd.read_csv('c:/projects of python/iris project/iris.csv')
print(df.head())
df.to_csv('c:/projects of python/iris project/new_iris.csv', index=False)
print("DataFrame has been written to 'new_iris.csv'.")












