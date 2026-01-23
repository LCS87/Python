import pandas as pd
import re
def formatar_telefone(numero):
    return ''.join(filter(str.isdigit, str(numero)))
# Carregar as planilhas
planilha1 = pd.read_excel(r"C:\Users\Avantti\Desktop\bko.xlsx")
planilha2 = pd.read_excel(r"C:\Users\Avantti\Desktop\RelatorioInfoB2B_Logistica_20240307134638.xlsx")

# Loop sobre cada pessoa na planilha1
for index, row in planilha1.iterrows():
    CNPJ = row['EMPRESA']
    if CNPJ[0].isdigit():
        CNPJ = ' '.join(CNPJ.split()[1:])
    else:
        CNPJ = CNPJ


    # Procurar o nome na planilha2
    pessoa_na_planilha2 = planilha2.loc[planilha2['GRUPOECONOMICO'] == CNPJ]

    if not pessoa_na_planilha2.empty:
        # Extrair informações relevantes
        entrega_efetiva = pessoa_na_planilha2.iloc[0]['ENTREGA_EFETIVA']
        limite_entrega_prazo = pessoa_na_planilha2.iloc[0]['LIMITE_ENTREGA_NO_PRAZO']
        # Atualizar a planilha1
        if pd.notnull(entrega_efetiva):
            planilha1.at[index, 'DATA LIMITE ENTREGA'] = entrega_efetiva.strftime(
                '%d/%m/%Y')  # formatar para exibir apenas a data
        elif pd.notnull(limite_entrega_prazo):
            planilha1.at[index, 'DATA LIMITE ENTREGA'] = limite_entrega_prazo.strftime(
                '%d/%m/%Y')
    if not pessoa_na_planilha2['PERFORMANCE_PRIMEIRA_TENTATIVA'].empty:
        status = pessoa_na_planilha2.iloc[0]['PERFORMANCE_PRIMEIRA_TENTATIVA']
        planilha1.at[index, 'HISTÓRICO BKO'] = status
    else:
        planilha1.at[index, 'HISTÓRICO BKO'] = ''


    # Salvar a planilha1 atualizada
planilha1.to_excel(r'C:\Users\Avantti\Desktop\planilha1_atualizada.xlsx', index=False)