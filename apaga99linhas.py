import pandas as pd
from datetime import datetime
# Carrega a planilha
caminho_arquivo_csv = r"C:\Users\Avantti\Desktop\Novo volume\Beckap\operadora\MEIS DE 2022\COMPLETA\TESTE BRUNO  Obras de alvenaria M2\PARA APAGAR.csv" # Altere para o caminho da sua planilha
encodings = ['utf-8', 'latin1', 'iso-8859-1']
for encoding in encodings:
    try:
        df = pd.read_csv(caminho_arquivo_csv, encoding=encoding)
        break  # Se conseguiu ler com sucesso, interrompe o loop
    except UnicodeDecodeError:
        continue  # Se ocorrer um erro de decodificação, tenta o próximo encoding

# Remove as primeiras 99 linhas, começando da segunda linha (índice 1)
df = df.iloc[99:]
HORA = datetime.now()
caminho_planilha_sem_primeiras_linhas = r"C:\Users\Avantti\Desktop\Novo volume\Beckap\operadora\MEIS DE 2022\COMPLETA\TESTE BRUNO  Obras de alvenaria M2\PARA APAGAR.csv" # Altere para o caminho onde deseja salvar a planilha
df.to_csv(caminho_planilha_sem_primeiras_linhas, index=False)
print(HORA)
print("As primeiras 99 linhas foram removidas da planilha com sucesso.")

