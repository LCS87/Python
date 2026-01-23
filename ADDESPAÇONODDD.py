import pandas as pd
from tkinter import Tk, filedialog

# Abrir janela para escolher o arquivo de entrada
root = Tk()
root.withdraw()  # Ocultar a janela principal

file_path = filedialog.askopenfilename(title="Escolha o arquivo Excel", filetypes=[("Arquivos Excel", "*.xlsx;*.xls")])

if not file_path:
    print("Nenhum arquivo selecionado. Encerrando o programa.")
    exit()

# Ler o DataFrame do arquivo Excel
df = pd.read_excel(file_path)

# Função para formatar número de telefone
def formatar_numero_telefone(numero):
    if pd.notna(numero) and len(str(numero)) >= 2:
        numero_str = str(numero)
        ddd = numero_str[:2]
        resto = numero_str[2:]
        numero_formatado = f"{ddd} {resto}"
        return numero_formatado
    else:
        return numero

# Aplicar a função à coluna 'Telefone'
# Abrir janela para escolher o arquivo de saída
output_file_path = filedialog.asksaveasfilename(title="Salvar arquivo Excel formatado", defaultextension=".xlsx",
                                                 filetypes=[("Arquivos Excel", "*.xlsx")])

if not output_file_path:
    print("Nenhum arquivo de saída selecionado. Encerrando o programa.")
    exit()

# Salvar o DataFrame formatado no arquivo Excel de saída
df.to_excel(output_file_path, index=False)

print("Operação concluída com sucesso.")
