import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)
df4 = pd.read_csv('mydata1.csv', skiprows=[0,1], header=None)
print(df4.shape)
print(df4)
print(df4.columns)
