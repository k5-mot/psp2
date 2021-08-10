import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)


df5 = pd.read_csv('mydata1.csv', skiprows=[0], header=0, index_col=0)
print(df5)
print(df5.shape)
print(df5.index)
print(df5.index.name)
