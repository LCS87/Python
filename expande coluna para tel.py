import pandas as pd

def dividir_telefones_em_colunas(planilha_path):
    # Carrega a planilha do Excel
    df = pd.read_excel(planilha_path)

    # Divide os números de telefone na coluna 'telefone_1' em várias colunas
    df_telefones_divididos = df['telefone_1'].str.split(', ', expand=True)

    # Adiciona as novas colunas ao DataFrame original
    df = pd.concat([df, df_telefones_divididos], axis=1)

    # Remove a coluna 'telefone_1' original, se desejar
    # df = df.drop('telefone_1', axis=1)

    # Salva a nova planilha com os números de telefone divididos
    df.to_excel(planilha_path, index=False)

# Substitua 'caminho/para/sua/planilha.xlsx' pelo caminho do seu arquivo Excel
dividir_telefones_em_colunas(r"C:\Users\TIava\OneDrive\Área de Trabalho\33K NORDESTE TIM\SEM VIABILIDADE\TIM NORD GERAL 281223.xlsx")