import pandas as pd

df = pd.read_excel(r"D:\Novo volume\Beckap\operadora\ACIMA DE MEI, 062024\PARA APAGAR.xlsx")

df['Telefone'] = df['Telefone'].astype(str)

df['Telefone'] = df['Telefone'].str.replace(r'\.0$', '', regex=True)

df.to_excel(r"D:\Novo volume\Beckap\operadora\ACIMA DE MEI, 062024\PARA APAGAR.xlsx", index=False)

