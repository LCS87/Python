import pandas as pd

# Carrega as duas planilhas
caminho_planilha1 = r"C:\Users\Downloads\PLANILHA CAR AGENTE HABILITADOR 12.12 normal.xlsx"
caminho_planilha2 = r"C:\Users\Downloads\Parque suspenso quantidade de dias.xlsx"

df1 = pd.read_excel(caminho_planilha1)
df2 = pd.read_excel(caminho_planilha2)

df1 = pd.read_excel(caminho_planilha1, dtype={'CNPJ_CLIENTE': str})
df2 = pd.read_excel(caminho_planilha2, dtype={'CNPJ_CLIENTE': str})

# Realiza a comparação das colunas de telefone
telefones_em_comum = df1[df1['CNPJ_CLIENTE'].isin(df2['CNPJ_CLIENTE'])]

# Adiciona as linhas com telefones em comum à planilha 2
df2 = df2.merge(telefones_em_comum, on='CNPJ_CLIENTE', how='left', suffixes=('_planilha2', '_planilha1'))

# Salva a planilha 2 com as novas linhas adicionadas
caminho_planilha2_atualizada = (r"C:\Users\Downloads\Result.xlsx")
df2.to_excel(caminho_planilha2_atualizada, index=False)