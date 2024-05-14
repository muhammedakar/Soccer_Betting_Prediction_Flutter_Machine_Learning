import pandas as pd

pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.max_column', None)
pd.set_option('display.width', 500)

df = pd.read_csv('dataset/iddiaaa.csv', delimiter=';',
                 names=['Week', 'Home', 'Away', 'Referee', 'Home_Value', 'Away_Value', 'Home_Atk', 'Home_Ort',
                        'Home_Def', 'Home_Gen', 'Away_Atk', 'Away_Ort', 'Away_Def', 'Away_Gen', 'Home_Bet', 'Draw_Bet', 'Away_Bet',
                        'Total_Goal', 'Alt_Bet', 'Ust_Bet', 'Ust', 'Home_Goal', 'Away_Goal',  'Target'])



df.drop(0, inplace=True)

df.reset_index(inplace=True, drop=True)

df['Home_Value'] = df['Home_Value'].str.replace(',', '.', regex=False)
df['Away_Value'] = df['Away_Value'].str.replace(',', '.', regex=False)

df.head()

ins = ['Week', 'Home_Atk', 'Home_Ort', 'Home_Def', 'Home_Gen', 'Away_Atk', 'Away_Ort', 'Away_Def', 'Away_Gen',
       'Total_Goal', 'Home_Goal', 'Away_Goal', 'Ust', 'Target']

flo = ['Alt_Bet', 'Ust_Bet', 'Home_Value', 'Away_Value']

for col in ins:
    df[col] = df[col].astype(int)

for col in flo:
    df[col] = df[col].astype(float)

df.info()

puan_durumu = {}

for index, row in df.iterrows():
    if row["Target"] == 1:  # Ev sahibi kazandıysa
        if row["Home"] not in puan_durumu:
            puan_durumu[row["Home"]] = 3
        else:
            puan_durumu[row["Home"]] += 3
        if row["Away"] not in puan_durumu:
            puan_durumu[row["Away"]] = 0
    elif row["Target"] == 2:  # Deplasman kazandıysa
        if row["Away"] not in puan_durumu:
            puan_durumu[row["Away"]] = 3
        else:
            puan_durumu[row["Away"]] += 3
        if row["Home"] not in puan_durumu:
            puan_durumu[row["Home"]] = 0
    else:  # Berabere kaldılarsa
        if row["Home"] not in puan_durumu:
            puan_durumu[row["Home"]] = 1
        else:
            puan_durumu[row["Home"]] += 1
        if row["Away"] not in puan_durumu:
            puan_durumu[row["Away"]] = 1
        else:
            puan_durumu[row["Away"]] += 1

    # O haftanın puanlarını ilgili satıra ekleyin
    df.at[index, 'Home_Point'] = puan_durumu.get(row["Home"], 0)
    df.at[index, 'Away_Point'] = puan_durumu.get(row["Away"], 0)

df.to_csv('dataset/iddiaa.csv',index_label=False,index=False)
