import pandas as pd

df = pd.read_excel(r"F:\Beckap\PARA SISTEM MEIS\MALLING MEI NE JUL A NOV 23\COMPLETAS\ME PL2\ME PL2 120324.xlsx")
for index, row in df.iterrows():
    nome = row['nome']
    razao = row['razao_social']


    if '-' in nome:
        df.at[index, 'nome'] = razao


print('O nome foi mudado')

df.to_excel(r"F:\Beckap\PARA SISTEM MEIS\MALLING MEI NE JUL A NOV 23\COMPLETAS\ME PL2\ME PL2 120324 teste.xlsx", index = False)

