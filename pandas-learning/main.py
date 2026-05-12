import pandas as pd

df = pd.read_csv('customers.csv')

print('df - Displays the entire DataFrame')
print(df)  # Display the entire DataFrame
      
print('head() - Returns the first 5 rows of the DataFrame')
print(df.head())

print('tail() - Returns the last 5 rows of the DataFrame')
print(df.tail())

print('info() - Shows column names, data types, and non-null counts')
df.info()

print('describe() - Shows statistical summary like mean, std, min, max for numeric columns')
print(df.describe())

print('columns - Lists all column names in the DataFrame')
print(df.columns)

print('index - Shows the row index range of the DataFrame')
print(df.index)