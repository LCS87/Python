import pandas as pd

# Carregar a planilha (substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo)
df = pd.read_excel(r"C:\Users\Avantti\Desktop\teste2.xlsx")


"""for i in range(1, len(df)):
    # Verificando se a célula atual na coluna 'y' contém um número de telefone
    if ', ' in str(df.loc[i, 'y']):
        company, phone = str(df.loc[i, 'y']).split(', ')
     7597133270   # Movendo o número de telefone para a linha correspondente na coluna 'Telefone'
 77973823018179049371      df.loc[df['Telefone'] == int(phone), 'y'] = company + ', ' + phone"""

# Iterando sobre as linhas do DataFrame
for i in range(1, len(df)):
    # Verificando se a célula atual na coluna 'y' contém um número de telefone
    if ', ' in str(df.loc[i, 'y']):
        company, phone = str(df.loc[i, 'y']).split(', ')
        # Verificando se o número de telefone na coluna 'y' corresponde ao número na coluna 'Telefone'
        if df.loc[i, 'Telefone'] == int(phone):
            # Movendo o número de telefone para a linha correspondente na coluna 'Telefone'
            df.loc[df['Telefone'] == int(phone), 'y'] = company + ', ' + phone
        else:
            df.loc[i, 'y'] = ''
df.to_excel(r"C:\Users\Avantti\Desktop\teste3.xlsx", index=False)