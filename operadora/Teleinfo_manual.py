import pandas as pd
import pyautogui as py
from time import sleep
import clipboard
import pyperclip

df = pd.read_excel("F:\Beckap\operadora\MEIS DO MES 0923\SEM TESTE CAP\Copia.xlsx")

for index, row in df.iterrows():
    TEL = row['Telefone 1']

    py.click()