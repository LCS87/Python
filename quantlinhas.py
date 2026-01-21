import pandas as pd

pl = pd.read_excel(r"C:\Users\TIava\OneDrive\Área de Trabalho\EMPRESASMOVELPJ NE\CLARO\CLARO2-CELULAR.xlsx")

# Criar DataFrame
df = pd.DataFrame(pl['telefone_1'])

# Função para contar a quantidade de números em uma célula
def contar_numeros(celula):
    numeros = str(celula).split(', ')  # Certifique-se de converter para string para evitar problemas com valores nulos
    return len(numeros)

# Aplicar a função a cada célula da coluna 'Demais Números' e criar uma nova coluna chamada 'Qntd. Linhas'
df['Qntd. Linhas'] = df['telefone_1'].apply(contar_numeros)

# Exibir o DataFrame resultante
df.to_excel(r"C:\Users\TIava\OneDrive\Área de Trabalho\EMPRESASMOVELPJ NE\CLARO\CLARO3-CELULAR.xlsx", index=False)

