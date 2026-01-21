import pandas as pd

# Carregar o arquivo CSV contendo os números de telefone
# Substitua 'caminho_para_seu_arquivo.csv' pelo caminho do seu arquivo CSV
df = pd.read_excel('caminho_para_seu_arquivo.csv')

# Número de linhas por planilha
linhas_por_planilha = 134

# Dividir o DataFrame em partes de acordo com o número de linhas por planilha
partes = [df[i:i+linhas_por_planilha] for i in range(0, len(df), linhas_por_planilha)]

# Criar e salvar uma nova planilha para cada parte
for i, parte in enumerate(partes):
    nome_arquivo = f'parte_{i+1}.xlsx'  # Nome do arquivo para cada parte
    parte.to_excel(nome_arquivo, index=False)  # Salvar a parte atual como uma nova planilha Excel