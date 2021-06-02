import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)
df2 = pd.read_csv('mydata1.csv', skiprows=[0])
print(df2.shape)
print(df2)
print(df2.columns)
print(type(df2.columns))
