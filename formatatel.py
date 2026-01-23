import pandas as pd

df = pd.read_excel(r"C:\Users\TIava\OneDrive\Área de Trabalho\GERAM NORD UM MILHAO\MEIS 072023\Operadoa ACIMA DOS 10K.xlsx")


def formatar_telefone(telefone):
    # Remover caracteres não numéricos
    numeros = ''.join(filter(str.isdigit, str(telefone)))

    # Verificar se o número tem mais de 10 dígitos
    if len(numeros) > 10:
        # Remover o último dígito para ter 10 dígitos
        numeros = numeros[-10:]

    # Formatando o número no estilo (XX) XXXX-XXXX
    telefone_formatado = f'({numeros[:2]}) {numeros[2:6]}-{numeros[6:]}'
    return telefone_formatado


# Aplicar a formatação à coluna 'telefone'
df['TELEFONE'] = df['TELEFONE'].apply(formatar_telefone)

# Salvar o DataFrame modificado em um novo arquivo Excel
novo_arquivo_excel = r"C:\Users\TIava\OneDrive\Área de Trabalho\GERAM NORD UM MILHAO\MEIS 072023\Operadoa ACIMA DOS 10K.xlsx"
df.to_excel(novo_arquivo_excel, index=False)