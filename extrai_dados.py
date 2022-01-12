#!/usr/bin/python3

import pandas as pd

df_final = pd.DataFrame()

def choose_uf(df, row):
    if df['UF_2021'][row] == df['UF_2021'][row]:
        return df['UF_2021'][row]
    return df['UF_2018'][row]

for estado in ["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO","Exterior"]:
# for estado in ["AC"]:

    print(f"Processando dados do estado {estado}")

    df_2018 = pd.read_csv(f'estados/{estado}_2018.csv', sep=";")
    df_2021 = pd.read_csv(f'estados/{estado}_2021.csv', sep=";")

    df_2018 = df_2018.replace('PATRI', 'PATRIOTA')
    df_2018 = df_2018.replace('PC DO B', 'PCDOB')
    df_2018 = df_2018.replace('SD', 'SOLIDARIEDADE')
    df_2018 = df_2018.replace('PR', 'PL')
    df_2018 = df_2018.replace('PRB', 'REPUBLICANOS')
    df_2018 = df_2018.replace('PPS', 'CIDADANIA')
    df_2018 = df_2018.replace('PR', 'PL')

    df_2021 = df_2021.replace('PATRI', 'PATRIOTA')
    df_2021 = df_2021.replace('PC DO B', 'PCDOB')
    df_2021 = df_2021.replace('SD', 'SOLIDARIEDADE')
    df_2021 = df_2021.replace('PR', 'PL')
    df_2021 = df_2021.replace('PRB', 'REPUBLICANOS')
    df_2021 = df_2021.replace('PPS', 'CIDADANIA')
    df_2021 = df_2021.replace('PR', 'PL')

    df_2018 = df_2018.replace('ZZ', 'EXTERIOR')
    df_2021 = df_2021.replace('ZZ', 'EXTERIOR')

    ids = list()
    for row in df_2018.index:
        ids.append(f"{df_2018['Abrangência'][row]}_{df_2018['Partido'][row]}")
    df_2018['id'] = ids

    ids = list()
    for row in df_2021.index:
        ids.append(f"{df_2021['Abrangência'][row]}_{df_2021['Partido'][row]}")
    df_2021['id'] = ids

    df_cmp = pd.merge(df_2021, df_2018, on='id', how='outer', suffixes=('_2021', '_2018'))

    df_cmp['Eleitores_2018'] = df_cmp['Eleitores_2018'].fillna(0)
    df_cmp['Eleitores_2021'] = df_cmp['Eleitores_2021'].fillna(0)

    df_cmp.to_excel('teste.xlsx')

    for row in df_cmp.index:
        abrangencia = df_cmp['id'][row].split("_")[0]
        partido = df_cmp['id'][row].split("_")[1]
        eleitores_18 = int(df_cmp['Eleitores_2018'][row])
        eleitores_21 = int(df_cmp['Eleitores_2021'][row])

        if abrangencia != 'TOTAL':
            new_row = {
                'Abrangência': abrangencia,
                'UF': choose_uf(df_cmp, row),
                'Partido': partido,
                'Filiados 2021': eleitores_21,
                'Filiados 2018': eleitores_18,
                'Diferença': eleitores_21 - eleitores_18
            }
            df_final = df_final.append(new_row, ignore_index=True)

df_final.to_excel('filiados_por_municipio.xlsx')