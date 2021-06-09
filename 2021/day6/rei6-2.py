import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

df1= pd.read_csv('mydata1.csv', skiprows=[0])
print(type(df1))
print(df1)
           # mydata1.csv
print(df1.shape)
