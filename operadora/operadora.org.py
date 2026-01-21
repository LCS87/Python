from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from time import sleep
import pyautogui as py
import re
def adicionar_nove(telefone):
    # Verifica se o número de telefone tem pelo menos 2 dígitos
    if len(telefone) >= 2:
        # Adiciona o número 9 após os dois primeiros dígitos
        telefone_formatado = telefone[:2] + '9' + telefone[2:]
        return telefone_formatado
    else:
        # Retorna o número de telefone original se tiver menos de 2 dígitos
        return telefone

def format_telefone(telefone):
    # Se o valor não for uma string, converter para string
    if not isinstance(telefone, str):
        telefone = str(telefone)

    # Remover espaços em branco antes e depois
    telefone = telefone.strip()

    # Remover caracteres não numéricos
    telefone = re.sub(r'\D', '', telefone)

    # Se o número de telefone tiver mais de 11 dígitos, remover o último dígito
    if len(telefone) > 11:
        telefone = telefone[:-1]

    return telefone
# Carrega o arquivo Excel
df = pd.read_excel(r"F:\Beckap\operadora\MEIS DO MES 0923\SEM TESTE CAP\Copia.xlsx")

# Substitua 'seuarquivo.xlsx' pelo caminho 51098866000118 do seu arquivo Excel
# e 'nomedasuaplanilha' pelo nome real da sua planilha.

# Escolhe a coluna desejada (por exemplo, coluna 'Nome')
# Substitua pelo nome da sua coluna
url = 'https://www.qualoperadora.org/'
navegador = Firefox()
indices_para_atualizar = []
navegador.get(url)
indice = 0
while len(navegador.find_elements(By.XPATH, '//*[@id="number"]')) < 1:
    pass
# Itera sobre os valores da coluna
for index, row in df.iterrows():
    TEL = format_telefone(row['Telefone 1'])
    TEL = adicionar_nove(TEL)


    try:
        WebDriverWait(navegador, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="dismiss-button"]/div/svg'))
        )
        anuncio = navegador.find_elements(By.XPATH, '//*[@id="dismiss-button"]/div/svg')
        if len(anuncio) > 0:
            anuncio[0].click()
    except:
        print('sem propaganda amém')

        # Use 'xpath' como a estratégia de localização
    while len(navegador.find_elements(By.XPATH, '//*[@id="number"]')) < 1:
        pass
    try:
        input = navegador.find_elements(By.XPATH, '//*[@id="number"]')
        if len(input) > 0:
            input[0].send_keys(TEL)
    except:
        print('faltou algo aqui!! vou atualizar')
        sleep(1)
        py.press('f5')

    while len(navegador.find_elements(By.XPATH, '//*[@id="go"]')) < 1:
        pass
    try:
        buscar = navegador.find_elements(By.XPATH, '//*[@id="go"]')
        sleep(1)
        if len(buscar) > 0:
            buscar[0].click()
    except:
        print('faltou algo aqui!! vou atualizar')
        sleep(1)
        py.press('f5')


    try:
        WebDriverWait(navegador, 4).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="feedback-button-yes"]'))
        )
        yes = navegador.find_elements(By.XPATH, '//*[@id="feedback-button-yes"]')
        c = 0
        while c != 10:
            try:
                WebDriverWait(navegador, 4).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="feedback-button-yes"]'))
                )
                sleep(3)
                yes = navegador.find_elements(By.XPATH, '//*[@id="feedback-button-yes"]')
                if len(yes) > 0:
                    navegador.get(url)
                    # Use 'xpath' como a estratégia de localização
                    while len(navegador.find_elements(By.XPATH, '//*[@id="number"]')) < 1:
                        pass

                    input = navegador.find_elements(By.XPATH, '//*[@id="number"]')
                    if len(input) > 0:
                        input[0].send_keys(TEL)

                    while len(navegador.find_elements(By.XPATH, '//*[@id="go"]')) < 1:
                        pass

                    buscar = navegador.find_elements(By.XPATH, '//*[@id="go"]')
                    sleep(1)
                    if len(buscar) > 0:
                        buscar[0].click()

                else:
                    c = 10
            except:
                sleep(1)
                c = 10

    except:
        sleep(1)

    try:
        WebDriverWait(navegador, 35).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/main/div/p'))
        )
        elementos_imagem = navegador.find_elements(By.XPATH, '/html/body/main/div/p')
        for elemento_imagem in elementos_imagem:
            mensagem = elemento_imagem.text.strip()  # Obtém o texto do elemento e remove espaços em branco extras
            primeira_palavra = mensagem.split()[0]  # Divide a mensagem em palavras e pega a primeira palavra
            print('Primeira palavra:', primeira_palavra)
            if len(primeira_palavra) > 0:
                py.click(561,305)
                py.write(f'{primeira_palavra}, {TEL}')
                sleep(1)
                py.click(1910,957)
                continue

    except:
        sleep(1)

    navegador.get(url)
    indice = indice + 1
    print(indice)

