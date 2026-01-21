from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from time import sleep
import pyautogui as py
import re

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
url = 'https://www.tim.com.br/sobre-a-tim/regulatorio/consulta-numero-tim'
navegador = Firefox()
indices_para_atualizar = []
navegador.get(url)
indice = 0
sleep(10)
while len(navegador.find_elements(By.XPATH, '//*[@id="numero"]')) < 1:
    pass
# Itera sobre os valores da coluna
for index, row in df.iterrows():
    TEL = format_telefone(row['Telefone 1'])

"""
    try:
        WebDriverWait(navegador, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="dismiss-button"]/div/svg'))
        )
        anuncio = navegador.find_elements(By.XPATH, '//*[@id="dismiss-button"]/div/svg')
        if len(anuncio) > 0:
            anuncio[0].click()
    except:
        print('sem propaganda')
"""
        # Use 'xpath' como a estratégia de localização
for c in range(30):
    py.sleep(10)
    try:
        input = navegador.find_elements(By.XPATH, '//*[@id="edit-phone-filter"]')
        if len(input) > 0:
            input[0].send_keys('81999504739')
        print('tentei')
    except:
        print('faltou algo aqui!! vou atualizar')
        sleep(1)
        py.press('f5')

    while len(navegador.find_elements(By.XPATH, '//*[@id="edit-submit-numero-tim"]')) < 1:
        pass
    try:
        buscar = navegador.find_elements(By.XPATH, '//*[@id="edit-submit-numero-tim"]')
        sleep(1)
        if len(buscar) > 0:
            buscar[0].click()
        print('tentei')
    except:
        print('faltou algo aqui!! vou atualizar')
        sleep(1)
        py.press('f5')

    """try:
        WebDriverWait(navegador, 4).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="dismiss-button"]/div/svg'))
        )
        anuncio = navegador.find_elements(By.XPATH, '//*[@id="dismiss-button"]/div/svg')
        if len(anuncio) > 0:
            anuncio[0].click()
    except:
        print('sem propaganda amém')
        
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
                    while len(navegador.find_elements(By.XPATH, '//*[@id="numero"]')) < 1:
                        pass

                    input = navegador.find_elements(By.XPATH, '//*[@id="numero"]')
                    if len(input) > 0:
                        input[0].send_keys(TEL)

                    while len(navegador.find_elements(By.XPATH, '//*[@id="numero"]')) < 1:
                        pass

                    buscar = navegador.find_elements(By.XPATH, '//*[@id="numero"]')
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
"""

    try:
        # Aguarda até que os elementos estejam presentes
        WebDriverWait(navegador, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//*[@id="block-views-block-numero-tim-block-1"]/div/div/div/div/span')
            )
        )

        # Encontra todos os elementos no XPATH especificado
        elementos = navegador.find_elements(By.XPATH,
                                            '//*[@id="block-views-block-numero-tim-block-1"]/div/div/div/div/span')

        for elemento in elementos:
            # Extrai o texto completo do elemento
            texto = elemento.text.strip()

            # Verifica se o texto não está vazio
            if texto:
                print('Texto capturado:', texto)

                # Usa o texto capturado no comando de escrita
                py.click(561, 305)  # Posição do clique (use Selenium se possível)
                py.write(f'{texto}, {TEL}')  # Inclui a variável TEL
                sleep(1)
                py.click(1910, 957)  # Posição de outro clique

    except IndexError:
        print("Erro: texto extraído está vazio.")
    except Exception as e:
        print(f"Erro inesperado: {e}")



    navegador.get(url)
    indice = indice + 1
    print(indice)



