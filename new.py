import pandas as pd
import pyautogui as py
import clipboard
import pyperclip
import textwrap
from time import sleep

# Carregar o arquivo Excel
df = pd.read_excel(r"C:\Users\Desktop\Automação new\GERAL.xlsx")

# Verificar se a coluna 'OBS ROBÔ' existe, senão cria uma nova coluna
if 'OBS ROBÔ' not in df.columns:
    df['OBS ROBÔ'] = ""

# Converter explicitamente a coluna 'OBS ROBÔ' para string
df['OBS ROBÔ'] = df['OBS ROBÔ'].astype(str)

# Lista para armazenar atualizações
obs_updates = []

for index, row in df.iterrows():
    if row['STATUS'] in ["ROTA DE ENTREGA", "FINALIZADO"]:
        continue  # Pular para o próximo CNPJ

    cnpj = str(row['CNPJ'])  # Converter o CNPJ para string
    sleep(5)
    py.doubleClick(1278, 298)
    sleep(.5)
    py.write(cnpj)
    sleep(1)
    py.click(567, 675)
    sleep(3)
    py.click(374, 927)
    sleep(3)
    py.click(529, 302)
    sleep(.5)
    sleep(.5)
    py.click(959,544)
    sleep(1)
    for s in range(3):

        py.click(959,544)
        sleep(.1)

    pyperclip.copy('')  # Limpar o conteúdo do clipboard
    py.hotkey('ctrl', 'c')  # Copiar o conteúdo da tela
    status = clipboard.paste()  # Pegar o conteúdo do clipboard

    # Formatar o texto adequadamente
    texto = f'{cnpj}, {status}'
    obs_formatado = textwrap.fill(texto, width=80)  # Formata o texto com largura de 80 caracteres

    # Atualiza o DataFrame e armazena as mudanças
    df.at[index, 'OBS ROBÔ'] = obs_formatado
    obs_updates.append((index, obs_formatado))  # Armazenar as atualizações

    sleep(1)
    py.press('esc')
    sleep(1)
    py.press('esc')
    sleep(1)
    py.press('f5')

# Tenta salvar o DataFrame atualizado em um novo arquivo Excel
try:
    df.to_excel(r"C:\Users\Desktop\Automação new\GERAL result.xlsx", index=False)
    print("Arquivo salvo com sucesso!")
except Exception as e:
    print(f"Erro ao salvar o arquivo: {e}")