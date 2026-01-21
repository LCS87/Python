import pandas as pd

# Carregar a planilha fornecida
file_path = r"C:\Users\Avantti\Desktop\RESULT.xlsx"
planilha = pd.read_excel(file_path)

# Agrupar os dados pelo consultor
consultores_grupos = planilha.groupby('CONSULTOR')


# Função para encontrar os valores mais frequentes de Desc_Cnae_Primario e Capital_Social
def top_clientes_por_consultor(grupo):
    top_cnaes = grupo['Desc_Cnae_Primario'].value_counts().head(3).index.tolist()
    top_capital = grupo['Capital_Social'].value_counts().head(3).index.tolist()

    # Garantir que ambas as listas tenham o mesmo comprimento
    max_length = max(len(top_cnaes), len(top_capital))
    top_cnaes += [None] * (max_length - len(top_cnaes))
    top_capital += [None] * (max_length - len(top_capital))

    return pd.DataFrame({
        'Top_Desc_Cnae_Primario': top_cnaes,
        'Top_Capital_Social': top_capital
    })


# Aplicar a função para cada grupo de consultor
top_clientes = consultores_grupos.apply(top_clientes_por_consultor).reset_index(drop=True)
top_clientes.to_excel(r"C:\Users\Avantti\Desktop\RESULT.xlsx", index=False)
# Exibir os resultados
print(top_clientes)