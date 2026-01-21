import pandas as pd
import mysql.connector

# Conectar ao banco de dados MySQL
conexao = mysql.connector.connect(
    host="000.0.0.0",
    user="root",
    password="kkkkkkkk",
    database="BANCO_DE_MEIS"
)

# Substitua 'sua_tabela' pelo nome real da sua tabela
tabela = 'TABELA_GERAL'

# Consulta SQL para obter todos os dados da tabela
query = f"SELECT * FROM {tabela}"

# Ler os dados do MySQL em um DataFrame do pandas
df = pd.read_sql(query, conexao)

# Desconectar do banco de dados MySQL
conexao.close()

# Salvar o DataFrame como um arquivo Excel na área de trabalho
caminho_arquivo_excel = r"C:\Users\Avantti\Desktop\SQL.xlsx"  # Substitua pelo seu caminho desejado
df.to_excel(caminho_arquivo_excel, index=False)

print(f'Dados exportados para o arquivo Excel: {caminho_arquivo_excel}')