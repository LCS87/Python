import pandas as pd

# Certifique-se de que o caminho do arquivo está correto
excel_file_path = r"C:\Users\TIava\OneDrive\Área de Trabalho\operadora\100124\MEI 0623.xlsx"

# Leia o arquivo Excel
df = pd.read_excel(excel_file_path)

# Substitua espaços em branco na coluna 'telefone_1' por '9'
df['Telefone'] = df['Telefone'].str.replace(' ', '9')

# Escreva o DataFrame modificado de volta para um novo arquivo Excel
output_excel_path = r"C:\Users\TIava\OneDrive\Área de Trabalho\operadora\100124\MEI 0623.xlsx"
df.to_excel(output_excel_path, index=False)