import pandas as pd

def adicionar_nove(telefone):
    # Verifica se o número de telefone tem pelo menos 2 dígitos
    if len(telefone) >= 2:
        # Adiciona o número 9 após os dois primeiros dígitos
        telefone_formatado = telefone[:2] + '9' + telefone[2:]
        return telefone_formatado
    else:
        # Retorna o número de telefone original se tiver menos de 2 dígitos
        return telefone

def remove_nove(telefone):
    # Verifica se o número de telefone tem pelo menos 2 dígitos
    if len(telefone) >= 3:
        # Verifica se o terceiro dígito é igual a 9
        if telefone[2] == '9':
            # Remove o terceiro dígito
            telefone_formatado = telefone[:2] + telefone[3:]
            return telefone_formatado
        else:
            # Retorna o número de telefone original se o terceiro dígito não for igual a 9
            return telefone
    else:
        # Retorna o número de telefone original se tiver menos de 3 dígitos
        return telefone
# Carregar o arquivo Excel
caminho_arquivo = R"D:\Novo volume\Beckap\operadora\MEIS DO MES 0723\ATIVOS MEIS 0723.xlsx"
dados = pd.read_excel(caminho_arquivo, dtype=str)
# Aplicar a função à coluna de telefones
dados['Telefone'] =dados['Telefone'].astype(str)
dados['Telefone'] = dados['Telefone'].apply(adicionar_nove)
#dados['TELEFONE'] = dados['TELEFONE'].astype(str).replace('.0', '')

# Salvar o arquivo Excel modificado
caminho_arquivo_modificado = R"D:\Novo volume\Beckap\operadora\MEIS DO MES 0723\ATIVOS MEIS 0723.xlsx"
dados.to_excel(caminho_arquivo_modificado, index=False)

