import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

df3 = pd.read_csv('mydata1.csv', skiprows=[0,1])
print(df3.shape)
print(df3)
print(df3.columns)
