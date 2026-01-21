import pandas as pd

# Leitura da planilha existente
nome_arquivo_entrada = "C:\\Users\\TIava\\Downloads\\EMPRESAMOVELPJ -MA-PI-CE-RN-PB-PE-AL-SE-BA (1).xlsx"
dados = pd.read_excel(nome_arquivo_entrada)

# Lista de operadoras únicas
operadoras_unicas = dados['OPERADORA'].unique()

# Criar planilhas separadas para cada operadora
for operadora in operadoras_unicas:
    planilha_operadora = dados[dados['OPERADORA'] == operadora]
    nome_arquivo_saida = f"C:\\Users\\TIava\\OneDrive\\Área de Trabalho\\{operadora}.xlsx"
    planilha_operadora.to_excel(nome_arquivo_saida, index=False)

print("Planilhas separadas foram criadas com sucesso.")
