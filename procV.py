import pandas as pd

# Carrega as duas planilhas
caminho_planilha1 = r"C:\Users\Avantti\Desktop\teste.xlsx"
caminho_planilha2 = r"C:\Users\Avantti\Desktop\PARA PESQUISA.xlsx"

df1 = pd.read_excel(caminho_planilha1)
df2 = pd.read_excel(caminho_planilha2)

df1['CNPJ'] = df1['CNPJ'].astype(str)
df2['CNPJ'] = df2['CNPJ'].astype(str)

# Realiza a comparação das colunas de telefone
telefones_em_comum = df1[df1['CNPJ'].isin(df2['CNPJ'])]

# Adiciona as linhas com telefones em comum à planilha 2
df2 = df2.merge(telefones_em_comum, on='CNPJ', how='left', suffixes=('_planilha2', '_planilha1'))

# Salva a planilha 2 com as novas linhas adicionadas
caminho_planilha2_atualizada = r"C:\Users\Avantti\Desktop\RESULT.xlsx"
df2.to_excel(caminho_planilha2_atualizada, index=False)
