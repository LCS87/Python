import pandas as pd
import re
# Carregue o arquivo CSV (substitua 'seu_arquivo.csv' pelo nome do seu arquivo)
df = pd.read_excel(r"F:\Beckap\PARA SISTEM MEIS\MALLING MEI NE JUL A NOV 23\COMPLETAS\MEIS 2 0823 0502.xlsx")
# Limpe a coluna removendo caracteres não numéricos
df['capital'] = df['capital'].astype(str).apply(lambda x: re.sub(r'\D', '', x))

# Remova valores vazios
df = df[df['capital'] != '']

# Converta os valores para números inteiros..
df['capital'] = df['capital'].astype(int)

# Classifique os valores da coluna 'capital' em ordem crescente..
df_sorted = df.sort_values(by='capital')

df_sorted.to_excel(r"F:\Beckap\PARA SISTEM MEIS\MALLING MEI NE JUL A NOV 23\COMPLETAS\MEIS 3 0823 0502.xlsx")