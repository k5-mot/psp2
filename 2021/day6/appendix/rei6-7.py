import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

df = pd.read_csv('mydata2.csv', index_col=0)
print(df)

print(df['好きな動物'])
print(type(df['好きな動物']))

print(df['好きな動物'][2])
print(type(df['好きな動物'][2]))

print(df['好きな動物'][2:5])

print(df.describe(include='all'))

print(df.mean())
print(df.median())
#print(df.sdv())
print(df.quantile(0.25))
print(df.quantile([0.25,0.75]))

df['誕生月'] = df['誕生月'].astype('str')
listBirthMonth = list([str(x) for x in range(1,13)])
df['誕生月'] = pd.Categorical(df['誕生月'], categories=listBirthMonth)
print(df['誕生月'])

listCelery = list(['超嫌い','嫌い','ふつう','好き','超好き'])
df['セロリ嗜好']=pd.Categorical(df['セロリ嗜好'],categories=listCelery, ordered=True)
print(df['セロリ嗜好'])

df['セロリ嗜好度値']=df['セロリ嗜好'].cat.codes
print(df['セロリ嗜好度値'])

listAnimal = list(['ライオン','チータ','ペガサス','ゾウ','猿','狼','子守熊','虎','黒ひょう','ひつじ','たぬき','こじか'])
df['好きな動物'] = pd.Categorical(df['好きな動物'], categories=listAnimal, ordered=False)
df['動物占いの判定'] = pd.Categorical(df['動物占いの判定'], categories=listAnimal, ordered=False)
print(df['好きな動物'])

print(df['動物占いの判定'])

print(df.describe(include='all'))
