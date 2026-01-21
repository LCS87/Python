import pandas as pd
import os

# Caminho onde as planilhas estão armazenadas
caminho_pasta = r"D:\Novo volume\Beckap\planilhas cookpit\endereços liberados" # Substitua pelo seu caminho real

# Lista para armazenar os DataFrames
dataframes = []

# Loop para ler cada arquivo Excel na pasta
for arquivo in os.listdir(caminho_pasta):
    if arquivo.endswith(".xlsx"):  # Verifica se é um arquivo Excel
        caminho_arquivo = os.path.join(caminho_pasta, arquivo)
        df = pd.read_excel(caminho_arquivo)  # Lê o arquivo
        dataframes.append(df)

# Combina todos os DataFrames em um só
df_combinado = pd.concat(dataframes, ignore_index=True)

# Salva o DataFrame combinado em um novo arquivo Excel
caminho_saida = os.path.join(caminho_pasta, "planilha_unificada.xlsx")
df_combinado.to_excel(caminho_saida, index=False)

print(f"Planilha unificada criada com sucesso em: {caminho_saida}")