import pandas as pd

# Carregar a planilha (substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo)
planilha = pd.read_excel(r"C:\Users\Avantti\Desktop\TESTE CAPITAL 2.xlsx")

# Substitua 'codigo' e 'fiy' pelos nomes reais das suas colunas
#planilha = planilha[planilha['Número Temporário'].isin(planilha['Telefone'])]

# Filtrar as linhas na coluna 'codigo' que estão presentes na coluna 'fiy'
planilha = planilha[~planilha['fui'].isin(planilha['codigo'])]
# Salvar o resultado em uma nova planilha (opcional)
planilha.to_excel(r"C:\Users\Avantti\Desktop\TESTE CAPITAL 22.xlsx", index=False)

# Exibir o DataFrame resultante (opcional)
print(planilha['codigo'])
