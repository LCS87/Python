import pandas as pd

# Carregando a planilha completa
df = pd.read_excel(r"C:\Users\TIava\Downloads\Lista CNAE - 08_12_2023 (13_44_37).xlsx")  # Substitua 'sua_planilha.xlsx' pelo nome real do seu arquivo

# Dividindo a planilha em 10 partes
num_parts = 10
chunk_size = len(df) // num_parts

# Criando e salvando as planilhas menores
for i in range(num_parts):
    start_idx = i * chunk_size
    end_idx = (i + 1) * chunk_size if i < num_parts - 1 else len(df)

    # Criando uma planilha menor
    df_part = df.iloc[start_idx:end_idx, :]

    # Salvando a planilha menor
    df_part.to_excel(f"C:\\Users\\TIava\\OneDrive\\Área de Trabalho\\PARTES DA GERAL{i + 1}.xlsx", index=False)