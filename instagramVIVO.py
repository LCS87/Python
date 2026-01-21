
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




# Substitua 'seuarquivo.xlsx' pelo caminho correto do seu arquivo Excel
# e 'nomedasuaplanilha' pelo nome real da sua planilha.

# Escolhe a coluna dese,ASCASASCASa (por exemplo, coluna 'Nome')
# Substitua pelo nome da sua coluna
url = 'https://www.instagram.com/accounts/login/'
navegador = Firefox()
indices_para_atualizar = []
navegador.get(url)
indice = 0
while len(navegador.find_elements(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')) < 1:
    pass
login = navegador.find_elements(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
senha = navegador.find_elements(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
entrar = navegador.find_elements(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
if len(login) > 0:
    login[0].send_keys('vivocoorporativo')
    sleep(.5)
    senha[0].send_keys('kkkkkkkkkkk')
    sleep(.5)
    entrar[0].click()
while len(navegador.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div'))<1:
    pass
pesquisar = navegador.find_elements(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div')
if len(pesquisar) > 0:
    pesquisar[0].click()
while len(navegador.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input'))<1:
    pass
input = navegador.find_elements(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
if len(input) > 0:
    input[0].send_keys('vivo empresas')

while len(navegador.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[2]/div[1]/div/div'))<1:
    pass
obj = navegador.find_elements(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[2]/div[1]/div/div')
if len(obj) > 0:
    obj[0].click()

while len(navegador.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a'))<1:
    pass
seguidores = navegador.find_elements(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
if len(seguidores) > 0:
    seguidores[0].click()

while len(navegador.find_elements(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[2]/div/div/div/div[3]/div/button/div/div'))<1:
    pass
seguir = navegador.find_elements(By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[4]/div/div/div/div[3]/div/button')
c = 1
while True:
    for _ in range(500):
        xpath = f'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{c}]/div/div/div/div[3]/div/button/div/div'

        # Tentar encontrar elemento por até 10 segundos
        for _ in range(1):
            seguir = navegador.find_elements(By.XPATH, xpath)
            if seguir:
                seguir[0].click()
                try:
                    sleep(2)
                    cancel = navegador.find_elements(By.XPATH,'/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
                    if len(cancel)> 0:
                        cancel[0].click()
                except:
                    sleep(1)

                print(f'seguindo o {c}..')
                sleep(3)
                break  # Saia do loop interno se o elemento for encontrado
            else:
                sleep(1)
        c += 1  # Incrementa c dentro do loop de 30
        if c == 30:
            print('esperando....')
            sleep(300)
        if c == 60:
            print('esperando....')
            sleep(300)
        if c == 90:
            print('esperando....')
            sleep(300)
        if c == 120:
            print('esperando....')
            sleep(300)
        if c == 150:
            print('esperando....')
            sleep(300)
        if c == 180:
            print('esperando....')
            sleep(300)
        if c == 210:
            print('esperando....')
            sleep(300)
        if c == 240:
            print('esperando....')
            sleep(300)
        if c == 270:
            print('esperando....')
            sleep(300)
        if c == 300:
            print('esperando....')
            sleep(300)
        if c == 330:
            print('esperando....')
            sleep(300)
        if c == 360:
            print('esperando....')
            sleep(300)
        if c == 390:
            print('esperando....')
            sleep(300)
        if c == 420:
            print('esperando....')
            sleep(300)
        if c == 450:
            print('esperando....')
            sleep(300)
        if c == 480:
            print('esperando....')
            sleep(300)
        if c == 500:
            print('esperando....')
            sleep(300)

