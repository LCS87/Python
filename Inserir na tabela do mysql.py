import pandas as pd
import mysql.connector
from tkinter import Tk, filedialog

# Abrir a janela de diálogo para escolher a pasta
root = Tk()
root.withdraw()  # Esconder a janela principal

# Pedir ao usuário para escolher o arquivo Excel
file_paths = filedialog.askopenfilenames(title="Selecione o(s) arquivo(s) XLSX", filetypes=[("Arquivos XLSX", "*.XLSX")])

# Verificar se o usuário selecionou algum arquivo
if not file_paths:
    print("Nenhum arquivo Excel selecionado. O programa será encerrado.")
    exit()

# Iterar sobre os arquivos selecionados
for file_path in file_paths:
    # Ler o arquivo Excel usando pandas
    df = pd.read_excel(file_path)

    # Conectar ao banco de dados MySQL
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="33548084",
        database="banco_de_meis"
    )

    # Criar um cursor
    cursor = conexao.cursor()

    # Iterar sobre as linhas do dataframe
    for index, row in df.iterrows():
        # Converter valores NaN para None
        row = [None if pd.isna(value) else value for value in row]

        # Construir a consulta SQL com parâmetros dinâmicos
        colunas = ', '.join(df.columns)
        valores = ', '.join(['%s' for _ in range(len(row))])
        # Substitua 'sua_tabela' pelo nome real da sua tabela no banco de dados
        query = f"INSERT INTO vendas ({colunas}) VALUES ({valores})"

        # Executar a consulta com os parâmetros
        cursor.execute(query, row)

    # Confirmar as alterações
    conexao.commit()

    # Fechar a conexão
    conexao.close()

