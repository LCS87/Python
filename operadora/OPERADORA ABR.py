from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from time import sleep
import pyautogui as py
import re

url = 'https://tt7773.com/home/subgame?currency=BRL&id=243479818&gameCategoryId=3&platformId=200'
navegador = Firefox()
indices_para_atualizar = []
navegador.get(url)
indice = 0
while len(navegador.find_elements(By.XPATH, '//*[@id="form"]/div[1]/div[3]')) < 1:
    pass
for c in range(1):
    lista= []

    try:
        WebDriverWait(navegador, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="form"]/div[1]/div[3]'))
        )
        addPL = navegador.find_elements(By.XPATH, '//*[@id="form"]/div[1]/div[3]')
        if len(addPL) > 0:
            addPL[0].click()
    except:
        print('sem input')



    while len(navegador.find_elements(By.XPATH, '//*[@id="resultado"]/tbody/tr[1]/td[1]')) < 1:
        pass
    try:
        WebDriverWait(navegador, 300).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="resultado"]'))
        )
        tabela_html = navegador.find_elements(By.XPATH, '//*[@id="resultado"]')

            # Use Pandas para ler a tabela HTML
        df = pd.read_html(tabela_html)[0]  # Supondo que a tabela seja a primeira encontrada na página

            # Salve o DataFrame em um arquivo Excel
        df.to_excel(r"C:\Users\Avantti\Desktop\Teste.xlsx", index=False)
        print(df)
            # Encerre o driver do Selenium
    except:
        print('sem planilha')

