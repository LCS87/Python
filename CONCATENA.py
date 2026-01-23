import pandas as pd

df = pd.read_excel("C:\\Users\\TIava\\OneDrive\\Área de Trabalho\\OI-CELULAR.xlsx")

# Converta as colunas para string antes de concatenar
df['DDD'] = df['DDD'].astype(str)
df['TEL'] = df['TEL'].astype(str)

df['concatenado'] = df['DDD'] + df['TEL']

df.to_excel("C:\\Users\\TIava\\OneDrive\\Área de Trabalho\\OI-CELULAR 2.xlsx", index=False)