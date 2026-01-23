import pandas as pd

# Leia o arquivo Excel
df = pd.read_excel("C:\\Users\\TIava\\Desktop\\....xlsx")

df['TEL'] = df['TEL'].astype(str)

# Agrupe por DOC e agregue as colunas desejadas

# Agrupe por DOC e agregue as colunas desejadas
df_agrupado = df.groupby('DOC').agg({
    'TEL': lambda x: ', '.join(x),
    'Id': 'first',
    'DDD': 'first',
    'NOME': 'first',
    'TP_LOG': 'first',
    'LOGRAD': 'first',
    'NUMERO': 'first',
    'COMPLEM': 'first',
    'BAIRRO': 'first',
    'CIDADE': 'first',
    'UF': 'first',
    'CEP': 'first',
    'INST': 'first',
    'OPERADORA': 'first',
    'TDOC': 'first'
})

# Adiciona a coluna 'QtdTelefones' representando a quantidade de telefones para cada CNPJ
df_agrupado['QtdTelefones'] = df.groupby('DOC')['TEL'].transform('count').reset_index(drop=True)

# Reset index para obter um DataFrame plano
df_agrupado.reset_index(inplace=True)


df_agrupado.to_excel("C:\\Users\\TIava\\Desktop\\TIM NORD GERAL.xlsx", index=False)