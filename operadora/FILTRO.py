import pandas as pd

# Carregar dados das planilhas
planilha1 = pd.read_excel(r"C:\Users\\Desktop\Mallings para AURA\2024\VIVO MEI\MEIS VIVO DE 12 DE 2023 A 4 2024.xlsx")
planilha2 = pd.read_excel(r"D:\Novo volume\Beckap\planilhas cookpit\endereços liberados\planilha_unificada.xlsx")

# Assumindo que as colunas de CEP são chamadas 'CEP'
cep_planilha2 = planilha2['CEP']

# Filtrar valores de CEP presentes em ambas as planilhas
filtered_planilha1 = planilha1[planilha1['cep'].isin(cep_planilha2)]

# Opcional: Salvar os resultados em uma nova planilha

filtered_planilha1.to_excel(r"C:\Users\\Desktop\Mallings para AURA\2024\VIVO MEI\MEIS VIVO DE 12 DE 2023 A 4 2024 com via.csv", index=False)

print("Filtragem concluída e salva em 'filtered_planilha1.xlsx'.")
