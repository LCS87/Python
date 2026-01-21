import pandas as pd
from tkinter import Tk, filedialog

# Abrir a janela de diálogo para selecionar o arquivo CSV
root = Tk()
root.withdraw()  # Esconder a janela principal
file_paths = filedialog.askopenfilenames(title="Selecione o(s) arquivo(s) CSV", filetypes=[("Arquivos CSV", "*.CSV")])

# Verificar se o usuário selecionou algum arquivo
if not file_paths:
    print("Nenhum arquivo CSV selecionado. O programa será encerrado.")
    exit()

# Iterar sobre os arquivos selecionados
for file_path in file_paths:
    # Carregar a planilha
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        # Se não for possível ler com UTF-8, tente Latin-1
        try:
            df = pd.read_csv(file_path, encoding='latin1')
        except pd.errors.ParserError:
            print(f"Erro ao ler o arquivo: {file_path}")
            continue

    # Remover linhas que contêm valores NaN
    df_clean = df.dropna()

    # Salvar a planilha sem os valores NaN
    df_clean.to_csv(r"C:\Users\Avantti\Desktop\GERAL\sem_nan.csv", index=False)