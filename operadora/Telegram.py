import pandas as pd
import pyautogui as py
from time import sleep
import clipboard
import keyboard  # Adicionado para detecção de teclado
import pyperclip


def adicionar_nove(telefone):
    # Verifica se o número de telefone tem pelo menos 2 dígitos
    if len(telefone) >= 2:
        # Adiciona o número 9 após os dois primeiros dígitos
        telefone_formatado = telefone[:2] + '9' + telefone[2:]
        return telefone_formatado
    else:
        # Retorna o número de telefone original se tiver menos de 2 dígitos
        return telefone


# Função para verificar se o usuário pressionou o atalho de teclado para pausar
def check_pause():
    if keyboard.is_pressed('ctrl+shift+p'):  # Define o atalho para pausar como Ctrl+Shift+P
        input("O programa está pausado. Pressione Enter para continuar...")


# Alerta antes de iniciar
print("O programa vai começar em 5 segundos. Pressione Ctrl+Shift+P a qualquer momento para pausar.")

# Aguarda 5 segundos antes de iniciar
sleep(5)

# Leitura do arquivo Excel
df = pd.read_excel(r"F:\Beckap\operadora\ME\pl2\Copia.xlsx")
sleep(10)



# Loop através das linhas do dataframe
for index, row in df.iterrows():
    # Obtenção do número de telefone e formatação89934225574
    TEL = str(row['Telefone_1'])
    TEL = adicionar_nove(TEL)
    sleep(11)


    py.click(574,989)
    sleep(1)
    py.click(574,989)
    sleep(1)
    py.write(TEL)
    sleep(1)
    py.press('enter')
    sleep(.5)
    pyperclip.copy('')
    py.doubleClick(513,797)
    sleep(1)
    py.hotkey('ctrl','c')
    sleep(.5)
    operadora = clipboard.paste()
    while operadora == ':':
        py.doubleClick(513, 797)
        sleep(1)
        py.hotkey('ctrl', 'c')
        sleep(.5)
        operadora = clipboard.paste()
    py.click(1398,310)
    sleep(1)
    py.click(1398,310)
    sleep(1)
    py.write(TEL)
    sleep(1)
    py.click(1904,953)
    sleep(1)




