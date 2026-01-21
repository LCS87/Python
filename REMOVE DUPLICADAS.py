import pandas as pd

# Carregar a planilha
caminho_arquivo = r"C:\Users\wilgner.oliveira\Downloads\teste tres.xlsx"
df = pd.read_excel(caminho_arquivo)

# Remover duplicatas com base na coluna 'cnpj'
df_sem_duplicatas = df.drop_duplicates(subset=['cnpj'])

# Salvar o arquivo sem duplicatas
df_sem_duplicatas.to_excel(caminho_arquivo, index=False)

# Salvar o arquivo sem duplicatas
df_sem_duplicatas.to_excel(r"C:\Users\wilgner.oliveira\Downloads\teste tres.xlsx", index=False)

print("Duplicatas removidas e arquivo salvo.")