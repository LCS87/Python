import pandas as pd

def adicionar_valor_de_coluna(planilha_origem, planilha_destino, cnpj_coluna, coluna_origem, coluna_destino):
    # Carrega as planilhas do Excel
    df_origem = pd.read_excel(planilha_origem)
    df_destino = pd.read_excel(planilha_destino)

    # Itera sobre as linhas da planilha de origem
    for index, row in df_origem.iterrows():
        cnpj = row[cnpj_coluna]
        valor_origem = row[coluna_origem]

        # Encontra a linha correspondente na planilha de destino
        linha_destino = df_destino[df_destino[cnpj_coluna] == cnpj].index

        # Se a linha foi encontrada, adiciona o valor na coluna correspondente
        if not linha_destino.empty:
            df_destino.at[linha_destino[0], coluna_destino] = valor_origem

    # Salva a planilha de destino atualizada
    df_destino.to_excel(r"C:\Users\TIava\OneDrive\Área de Trabalho\EMPRESASMOVELPJ NE\TIM\TIM3-CELULAR.xlsx", index=False)

# Substitua 'caminho/para/sua/planilha_origem.xlsx' e 'caminho/para/sua/planilha_destino.xlsx'
# pelos caminhos reais dos seus arquivos Excel
adicionar_valor_de_coluna(r"C:\Users\TIava\Downloads\InfoB2B_1K.xlsx", r"C:\Users\TIava\OneDrive\Área de Trabalho\EMPRESASMOVELPJ NE\TIM\TIM3-CELULAR.xlsx", 'DOC', 'FLAGDISPO', 'FLAGDISPO')