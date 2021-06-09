import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

# Read database.
df = pd.read_csv('mydata2.csv', index_col=0)

# Categorize database
df['所持金額'] = df['所持金の増加（差）'] / (df['所持金の増加（比）'] - 1)

# Print results
# print(df[df['好きな動物']=='ライオン']['所持金額'])
# print(df[df['好きな動物']=='たぬき']['所持金額'])
means_lion = df[df['好きな動物'] == 'ライオン']['所持金額'].mean()
means_nook = df[df['好きな動物'] == 'たぬき']['所持金額'].mean()

print('ライオンの所持金平均: ' + str(means_lion))
print('たぬきの所持金平均  : ' + str(means_nook))
print()

if means_lion < means_nook:
  print('「好きな動物」が「たぬき」の人の所持金の平均が多い')
else:
  print('「好きな動物」が「ライオン」の人の所持金の平均が多い')
