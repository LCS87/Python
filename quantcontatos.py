import pandas as pd
import numpy as np
# Ler o arquivo Excel em um DataFrame
df = pd.read_excel("C:\\Users\\TIava\\OneDrive\\Área de Trabalho\\PARA SISTEM MEIS\\MEIS CLARO\\MEIS CLARO 11122023 PT2.xlsx")


# Aplicando a função para remover o último dígito nos números com 11 dígitos
df['Telefone'] = df['Telefone'].apply(lambda x: str(x)[:-1] if len(str(x)) == 11 else str(x))

# Sa


df.to_excel("C:\\Users\\TIava\\OneDrive\\Área de Trabalho\\PARA SISTEM MEIS\\MEIS CLARO\\MEIS CLARO 11122023 PT2.xlsx", index=False)