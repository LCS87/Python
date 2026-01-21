import pandas as pd

df = pd.read_excel(r"C:\Users\wilgner.oliveira\Desktop\CNAE COMPLETO\Empresas Socios\So os cnpj\cnpjs empresas abertas no mes 062024.xlsx")


def formatar_planilha(nome_arquivo):
    # Carregar o arquivo Excel
    df = pd.read_excel(nome_arquivo)

    # Aplicar a formatação desejada na coluna específica
    df['Sua_Coluna'] = df['Sua_Coluna'].str.split('-').str[0].str.strip()

    # Salvar as alterações no arquivo
    df.to_excel(nome_arquivo, index=False)


#df['nome'] = df['nome'].apply(lambda x: ' '.join(x.split()[:4]))

def formatar_valor(numero):
    return ''.join(filter(str.isdigit, str(numero)))

# Aplique a função à coluna de telefone
df['CNPJ'] = df['CNPJ'].apply(formatar_valor)
#df['cnpj'] = df['cnpj'].apply(formatar_valor)

# Supondo que você tenha um arquivo CSV chamado "dados.csv" com uma coluna chamada "Nomes"

# Separar apenas os nomes dos sócios
#df['Nome'] = df['Nome'].str.extract(r'([^-]+)')

# Salvar o resultado em um novo arquivo CSV ou substituir o original

df.to_excel(r"C:\Users\wilgner.oliveira\Desktop\CNAE COMPLETO\Empresas Socios\So os cnpj\cnpjs empresas abertas no mes 062024.xlsx", index=False)


