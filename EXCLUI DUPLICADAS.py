import pandas as pd

# Suponha que você tenha um DataFrame chamado df
df = pd.read_excel(r"C:\Users\TIava\OneDrive\Área de Trabalho\EMPRESASMOVELPJ NE\CLARO\CLARO-CELULAR.xlsx")
# Remova as linhas duplicadas

df = df.drop_duplicates(subset='DOC', keep='first')

df.to_excel(r"C:\Users\TIava\OneDrive\Área de Trabalho\EMPRESASMOVELPJ NE\CLARO\CLARO2-CELULAR.xlsx", index=False)
print(df['DOC'])