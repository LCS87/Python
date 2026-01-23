import pandas as pd
import re
# Carregue o arquivo Excel
df = pd.read_excel(r"F:\Beckap\operadora\MEIS DE MAIO PARA ATRAS 2023\160K PARA RODAR\SEM TESTE\IBRIDGE.xlsx")

# Função para extrair o primeiro número de telefone de uma string
"""def extrair_primeiro_numero(telefone):
    numeros = [parte for parte in telefone.split() if parte.isdigit()]
    return numeros[0] if numeros else ''"""
"""
# Aplique a função à coluna de números de telefone
df['Operadora'] = df['Operadora'].astype(str)
df['Operadora'] = df['Operadora'].apply(extrair_primeiro_numero)
"""
def extrair_string(valor):
    if isinstance(valor, str):
        return valor.split(',')[0].strip()
    else:
        return valor

#df['operadora'] = df['operadora'].apply(extrair_string)
def remover_digitos(texto):
    return re.sub('^\d+.\d+\s', '', texto)
df['nome'] = df['nome'].str[10:]


df.to_excel(r"F:\Beckap\operadora\MEIS DE MAIO PARA ATRAS 2023\160K PARA RODAR\SEM TESTE\IBRIDGE.xlsx", index=False)



