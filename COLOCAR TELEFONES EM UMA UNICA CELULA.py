import pandas as pd

df = pd.read_excel(r"C:\Users\Avantti\Desktop\VIVOCORP\2.5 RelatorioInfoB2B_ParqueMovel_20240318172816.xlsx")

# Converta a coluna 'TEL' para string
df['NR_TELEFONE'] = df['NR_TELEFONE'].astype(str)

# Crie um novo DataFrame com 'DOC' e 'TEL' concatenados
df_concatenado = df.groupby('CNPJ_CLIENTE')['NR_TELEFONE'].apply(', '.join).reset_index()
df_concatenado.columns = ['CNPJ_CLIENTE', 'TEL_concatenado']

# Junte o novo DataFrame ao DataFrame original
df_final = pd.merge(df, df_concatenado, on='CNPJ_CLIENTE')

df_final.to_excel(r"C:\Users\Avantti\Desktop\VIVOCORP\2.5 RelatorioInfoB2B_ParqueMovel_20240318172816.xlsx", index=False)
print(df_final)

