import pandas as pd

# Carregar os dados das planilhas
df1 = pd.read_excel(r"C:\Users\Avantti\Desktop\PARA PESQUISA.xlsx")  # Substitua 'planilha1.xlsx' pelo caminho do seu arquivo
df2 = pd.read_excel(r"C:\Users\Avantti\Desktop\teste.xlsx")  # Substitua 'planilha2.xlsx' pelo caminho do seu arquivo

# Função para limpar CNPJ


df2_relevantes = df2[['CNPJ', 'CONSULTOR', 'EMPRESA']]  # Substitua pelas colunas relevantes de df2

# Filtrar df1 com base na coluna CNPJ de df2 e mesclar com as colunas relevantes de df2
df_result = pd.merge(df1, df2_relevantes, on='CNPJ', how='inner')

# Exibir o resultado final com as colunas concatenadas

# Salvar o resultado final em um novo arquivo Excel
df_result.to_excel(R"C:\Users\Avantti\Desktop\RESULT.xlsx", index=False)