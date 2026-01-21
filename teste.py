import pandas as pd

df = pd.read_excel(r"C:\Users\Desktop\para subirR.xlsx")
df['cep'] = df['cep'].astype(str)
df['cep'] = df['cep'].str.replace('.0','')

df.to_excel(r"C:\Users\Desktop\para subirR.xlsx")