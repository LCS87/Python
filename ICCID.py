import pandas as pd

# Ler o arquivo CSV
df = pd.read_excel(r"C:\Users\Avantti\Downloads\Pasta1.xlsx")

# Preencher os valores de ICCID nas linhas em branco
df['ICCID'] = df['Service Id'].shift(-4)

# Remova as linhas onde 'Número' é NaN
df = df[df['Número de portabilidade'].notna()]

print(df)
# Salvar o arquivo atualizado
df.to_excel(r"C:\Users\Avantti\Downloads\Pasta11.xlsx", index=False)