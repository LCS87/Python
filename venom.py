import time
from lib2to3.pgen2 import driver
from selenium.common import TimeoutException
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pandas as pd
from time import sleep
import pyautogui as py



# Carrega o arquivo Excel
df = pd.read_excel("C:\\Users\\TIava\\OneDrive\\Área de Trabalho\\MEI11223 - Copia.xlsx")

# Substitua 'seuarquivo.xlsx' pelo caminho correto do seu arquivo Excel
# e 'nomedasuaplanilha' pelo nome real da sua planilha.

# Escolhe a coluna desejada (por exemplo, coluna 'Nome')
# Substitua pelo nome da sua coluna
url = 'https://qualoperadora.info/'
navegador = Firefox()
indices_para_atualizar = []
navegador.get(url)
indice = 0
while len(navegador.find_elements(By.XPATH, '//*[@id="tel"]')) < 1:
    pass

py.click(170,700)
sleep(1.5)
py.click(384,289)
# Itera sobre os valores da coluna
for index, row in df.iterrows():
    TEL = row['TELEFONE']

    try:
        WebDriverWait(navegador, 7).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="dismiss-button"]/div/svg'))
        )
        anuncio = navegador.find_elements(By.XPATH, '//*[@id="dismiss-button"]/div/svg')
        if len(anuncio) > 0:
            anuncio[0].click()
    except:
        print('sem propaganda amém')

        # Use 'xpath' como a estratégia de localização
    while len(navegador.find_elements(By.XPATH, '//*[@id="tel"]')) < 1:
        pass
    try:
        input = navegador.find_elements(By.XPATH, '//*[@id="tel"]')
        if len(input) > 0:
            input[0].send_keys(TEL)
    except:
        print('faltou algo aqui!! vou atualizar')
        sleep(1)
        py.press('f5')

    while len(navegador.find_elements(By.XPATH, '//*[@id="bto"]')) < 1:
        pass
    try:
        buscar = navegador.find_elements(By.XPATH, '//*[@id="bto"]')
        sleep(1)
        if len(buscar) > 0:
            buscar[0].click()
    except:
        print('faltou algo aqui!! vou atualizar')
        sleep(1)
        py.press('f5')

    try:
        WebDriverWait(navegador, 7).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="dismiss-button"]/div/svg'))
        )
        anuncio = navegador.find_elements(By.XPATH, '//*[@id="dismiss-button"]/div/svg')
        if len(anuncio) > 0:
            anuncio[0].click()
    except:
        print('sem propaganda amém')
    try:
        WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="feedback-button-yes"]'))
        )
        yes = navegador.find_elements(By.XPATH, '//*[@id="feedback-button-yes"]')
        c = 0
        while c != 10:
            try:
                WebDriverWait(navegador, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="feedback-button-yes"]'))
                )
                sleep(3)
                yes = navegador.find_elements(By.XPATH, '//*[@id="feedback-button-yes"]')
                if len(yes) > 0:
                    navegador.get(url)
                    # Use 'xpath' como a estratégia de localização
                    while len(navegador.find_elements(By.XPATH, '//*[@id="tel"]')) < 1:
                        pass

                    input = navegador.find_elements(By.XPATH, '//*[@id="tel"]')
                    if len(input) > 0:
                        input[0].send_keys(TEL)

                    while len(navegador.find_elements(By.XPATH, '//*[@id="bto"]')) < 1:
                        pass

                    buscar = navegador.find_elements(By.XPATH, '//*[@id="bto"]')
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
        WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/img'))
        )
    except:
        sleep(1)
    try:
        elementos_imagem = navegador.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/img')
        for elemento_imagem in elementos_imagem:
            titulo_da_imagem = elemento_imagem.get_attribute('title')
            print('Título da imagem:', titulo_da_imagem)
            if len(titulo_da_imagem) > 0:
                py.click(564,303)
                py.write(f'{titulo_da_imagem}, {TEL}')
                sleep(1)
                py.click(1904,956)

    except:
        sleep(1)
    try:
        elementos_imagem = navegador.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[2]/h2/b')

        if len(elementos_imagem) > 0:
            sleep(1)
            texto_do_elemento = elementos_imagem[0].text
            py.click(564,303)
            py.write(f'{texto_do_elemento}, {TEL}')
            sleep(1)
            py.click(1904,956)
        else:
            try:
                elementos_imagem = navegador.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[2]/p[1]/b')

                if len(elementos_imagem) > 0:
                    sleep(1)
                    texto_do_elemento = elementos_imagem[0].text
                    py.click(564,303)
                    py.write(f'{texto_do_elemento}, {TEL}')
                    sleep(1)
                    py.click(1904,956)


            except:
                py.click(564,303)
                sleep(1)
                py.write(f'obs, {TEL}')
                sleep(1)
                py.click(1904,956)

    except:
        sleep(1)

    navegador.get(url)
    indice = indice + 1
    print(indice)