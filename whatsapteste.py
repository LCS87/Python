import pandas as pd

df = pd.read_excel(r'C:\Users\Avantti\Desktop\planilha1_atualizada.xlsx')

# Converter a coluna 'DATA LIMITE ENTREGA' para o formato datetime
df['DATA LIMITE ENTREGA'] = pd.to_datetime(df['DATA LIMITE ENTREGA'], dayfirst=True)

# Formatando a data no estilo brasileiro
df['DATA LIMITE ENTREGA'] = df['DATA LIMITE ENTREGA'].dt.strftime('%d/%m/%Y')


df.to_excel(r'C:\Users\Avantti\Desktop\planilha2_atualizada.xlsx', index=False)