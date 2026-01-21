from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import pyautogui as py

url = 'https://api.whatsapp.com/send/?phone=8184231372&text&type=phone_number&app_absent=0'
navegador = Firefox()
indices_para_atualizar = []
navegador.get(url)
indice = 0
df = pd.read_excel('C:\\Users\\TIava\\OneDrive\\Área de Trabalho\\PARA SISTEM MEIS\\MEIS CLARO\\MEIS CLARO 11122023 PT2.xlsx')
while len(navegador.find_elements(By.XPATH,'//*[@id="app"]/div/div[2]/div[3]/header/div[1]')) < 1:
    pass


# Itera sobre os valores da coluna
for index, row in df.iterrows():
    TEL = row['Telefone']

    while len(navegador.find_elements(By.XPATH,
                                      '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[2]')) < 1:
        pass
    input = navegador.find_elements(By.XPATH,
                                    '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[2]')

    try:
        input[0].click()
        sleep(.6)
        py.write(TEL)
        sleep(.5)
        enviar = navegador.find_elements(By.XPATH,
                                         '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
        enviar[0].click()
    except Exception as e:
        print(f"Erro durante a interação: {e}")
        while len(navegador.find_elements(By.XPATH,'//*[@id="main"]/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div[1]/div[1]/div/div[1]/div/span[1]/span'))<1:
            pass
        numero = navegador.find_elements(By.XPATH,'//*[@id="main"]/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div[1]/div[1]/div/div[1]/div/span[1]/span')
        if len(numero)>0:
            numero[0].click()
            sleep(1.3)
            whatts = navegador.find_elements(By.XPATH,'//*[@id="app"]/div/span[5]/div/ul/div/li[1]/div')
            if len(whatts)>0:
                print(f'{TEL}, COM WHATTS.')

            else:
                print(f'{TEL}, SEM WHATTS.')
        while len(navegador.find_elements(By.XPATH,'//*[@id="main"]/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div[1]/span[2]/div/div/span'))<1:
            pass
        menu = navegador.find_elements(By.XPATH,'//*[@id="main"]/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div[1]/span[2]/div/div/span')
        if len(menu)>0:
            menu[0].click()
            while len(navegador.find_elements(By.XPATH,
                                              '//*[@id="app"]/div/span[5]/div/ul/div/li[7]/div')) < 1:
                pass
            apagar = navegador.find_elements(By.XPATH,
                                           '//*[@id="app"]/div/span[5]/div/ul/div/li[7]/div')
            if len(apagar) > 0:
                apagar[0].click()
                while len(navegador.find_elements(By.XPATH,
                                                  '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button[2]/div/div')) < 1:
                    pass
                apagado = navegador.find_elements(By.XPATH,
                                                 '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button[2]/div/div')
                if len(apagado) > 0:
                    apagado[0].click()
