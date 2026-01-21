from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from time import sleep
import re
import pandas as pd


def format_telefone(telefone):
    telefone = str(telefone).strip()
    telefone = re.sub(r'\D', '', telefone)  # Remove caracteres não numéricos
    if len(telefone) > 11:
        telefone = telefone[:-1]
    return telefone
c = 0
# Caminho do arquivo Excel
arquivo_entrada = r"D:\Novo volume\Beckap\operadora\MEIS DO MES 1223, 0124, 0224, 0324, 0424, 0524\selenium\arquivo04.xlsx"

# Carrega o arquivo Excel
df = pd.read_excel(arquivo_entrada)

# Adiciona uma coluna vazia para os resultados
df['resultado'] = ""

# URL da página
url = 'https://www.tim.com.br/sobre-a-tim/regulatorio/consulta-numero-tim'
navegador = Firefox()
navegador.get(url)
sleep(5)  # Aguarda o carregamento inicial da página

for index, row in df.iterrows():
    TEL = format_telefone(row['Telefone 1'])  # Formata o número
    try:
        # Processamento de entrada e busca
        input_field = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="edit-phone-filter"]'))
        )
        input_field.clear()
        input_field.send_keys(TEL)

        botao_buscar = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="edit-submit-numero-tim"]'))
        )
        sleep(.5)
        botao_buscar.click()

        resultado = WebDriverWait(navegador, 300).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="block-views-block-numero-tim-block-1"]/div/div/div/div/span')
            )
        )
        texto_resultado = resultado.text.strip()

        padrao = r'^O número.*rede TIM\.$'
        match = re.search(padrao, texto_resultado, re.MULTILINE)
        if match:
            resultado_final = match.group(0)
        else:
            resultado_final = "Resultado não encontrado"
        df.at[index, 'resultado'] = resultado_final

    except Exception as e:
        print(f"Erro no processo para o número {TEL}: {e}")
        df.at[index, 'resultado'] = "Erro na consulta"
    finally:
        navegador.get(url)  # Recarrega a página para a próxima consulta
        c += 1
        sleep(1)
        print(c)
        if c % 50 == 0:
            df.to_excel(r"D:\Novo volume\Beckap\operadora\MEIS DO MES 1223, 0124, 0224, 0324, 0424, 0524\selenium\resultado TIM teste.xlsx",
                index=False)
            print("Arquivo salvo com os resultados!")


# Salva o DataFrame atualizado em um novo arquivo Excel
df.to_excel(r"D:\Novo volume\Beckap\operadora\MEIS DO MES 1223, 0124, 0224, 0324, 0424, 0524\selenium\resultado TIM teste.xlsx", index=False)
print("Arquivo salvo com os resultados!")
