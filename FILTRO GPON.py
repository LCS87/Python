import pandas as pd

# Carregar o arquivo Excel original
caminho_arquivo_original = "caminho_para_o_arquivo_original.xlsx"
dados_original = pd.read_excel(caminho_arquivo_original)

# Filtrar as linhas onde a coluna 'Viabilidade' contém a palavra 'GPON'
dados_filtrados = dados_original[dados_original['Viabilidade'].str.contains('GPON', na=False)]

# Salvar as linhas filtradas em uma nova planilha Excel
caminho_arquivo_novo = "caminho_para_o_novo_arquivo.xlsx"
dados_filtrados.to_excel(caminho_arquivo_novo, index=False)



