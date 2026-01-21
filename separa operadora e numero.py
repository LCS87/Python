import pandas as pd

# Carregando a planilha
df = pd.read_excel(r"C:\Users\TIava\OneDrive\Área de Trabalho\operadora\MEI11223.xlsx")

# Dividindo a coluna "Telefone" em duas
df[['Operadora', 'Numero']] = df['Telefone'].str.extract('([a-zA-Z]+)(\d+)', expand=True)

# Removendo a coluna original "Telefone"
df = df.drop('Telefone', axis=1)

# Salvando a planilha atualizada
df.to_excel(r"C:\Users\TIava\OneDrive\Área de Trabalho\operadora\MEI11223 2.xlsx", index=False)  # Substitua 'seuarquivo_atualizado.csv' pelo nome desejado
