import pandas as pd
import pyodbc
from tkinter import Tk, filedialog


# Ler o arquivo Excel usando pandas
df = filedialog.askopenfilenames(title="Selecione o(s) arquivo(s) CSV", filetypes=[("Arquivos CSV", "*.CSV")])
# Conectar ao banco de dados
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=AVANTTITI;DATABASE=geral_nordeste;Trusted_Connection=yes')
# Criar um cursor

# Criar um cursor
cursor = conn.cursor()

# Iterar sobre as linhas do dataframe
for index, row in df.iterrows():
    # Construir a consulta SQL com parâmetros dinâmicos
    columns = ', '.join(f'[{col}]' for col in row.index)
    placeholders = ', '.join(['?' for _ in range(len(row))])

    query = f"INSERT INTO IBRIDGE_MEIS_MES4 ({columns}) VALUES ({placeholders})"

    # Executar a consulta com os parâmetros
    cursor.execute(query, tuple(row))

# Confirmar as alterações
conn.commit()

# Fechar a conexão
conn.close()