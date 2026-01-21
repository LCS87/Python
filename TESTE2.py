import pandas as pd

# Lê o arquivo CSV
df = pd.read_excel(r"C:\Users\Avantti\Desktop\Novo(a) Planilha do Microsoft Excel.xlsx")

# Converte as colunas de data para o formato adequado
df['FECHAMENTO'] = pd.to_datetime(df['DATA_FECHAMENTO']).dt.strftime('%Y-%m-%d')
df['DATA_BKO'] = pd.to_datetime(df['DATA_BKO']).dt.strftime('%Y-%m-%d')
df['FECHAMENTO'] = pd.to_datetime(df['FECHAMENTO']).dt.strftime('%Y-%m-%d')
df['DATA_COBRANÇA'] = pd.to_datetime(df['DATA_COBRANÇA']).dt.strftime('%Y-%m-%d')
df['DATA_LIMITE_ENTREGA'] = pd.to_datetime(df['DATA_LIMITE_ENTREGA']).dt.strftime('%Y-%m-%d')
df['DATA_ATV'] = pd.to_datetime(df['DATA_ATV']).dt.strftime('%Y-%m-%d')
df['DATA_PORTIN'] = pd.to_datetime(df['DATA_PORTIN']).dt.strftime('%Y-%m-%d')


# Adicione outras colunas de data conforme necessário

# Salva o arquivo CSV de volta
df.to_excel(r"C:\Users\Avantti\Desktop\Novo(a) Planilha do Microsoft Excel.xlsx", index=False)

