import pandas as pd
from datetime import datetime


# Carrega a planilha
caminho_arquivo = r"D:\Novo volume\Beckap\operadora\MEIS DO MES 1223, 0124, 0224, 0324, 0424, 0524\selenium\teste TIM.xlsx"# Altere para o caminho da sua planilha
encodings = ['utf-8', 'latin1', 'iso-8859-1']
for encoding in encodings:
    try:
            df = pd.read_csv(caminho_arquivo, encoding=encoding)
            break  # Se conseguiu ler com sucesso, interrompe o loop
    except UnicodeDecodeError:
        continue  # Se ocorrer um erro de decodificação, tenta o próximo encoding

# Remove as primeiras 99 linhas, começando da segunda linha (índice 1)
df = df.iloc[499:]
HORA = datetime.now()
caminho_planilha_sem_primeiras_linhas = r"D:\Novo volume\Beckap\operadora\MEIS DO MES 1223, 0124, 0224, 0324, 0424, 0524\selenium\teste TIM.xlsx" # Altere para o caminho onde deseja salvar a planilha
df.to_excel(caminho_planilha_sem_primeiras_linhas, index=False)
print(HORA)
print("As primeiras 499 linhas foram removidas da"
      "]+"
      ",planilha com sucesso.")

