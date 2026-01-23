import smtplib
import textwrap
import clipboard
import pandas as pd
from time import sleep
import pyautogui as py

def enviar_email(msg):
    corpo_email = """
    <p>Mudança de estatos!</p>
    <p></p>
    """

    msg_email = email.message.Message()
    msg_email['Subject'] = f" {msg}"
    msg_email['From'] = 'wilgneroliveirawil@gmail.com'
    msg_email['To'] = 'wilgneroliveirawil@gmail.com'
    password = 'yqtv beau rwhv nfhf'
    msg_email.add_header('Content-Type', 'text/html')
    msg_email.set_payload(corpo_email)

    s = smtplib.SMTP('smtp-mail.outlook.com: 587')
    s.starttls()
    s.login(msg_email['From'], password)
    s.sendmail(msg_email['From'], [msg_email['To']], msg_email.as_string().encode('utf-8'))
    print('Email enviado')

def formatar_telefone(numero):
    return ''.join(filter(str.isdigit, str(numero)))

# Carrega o arquivo Excel
df = pd.read_excel(r"C:\Users\Avantti\Desktop\Novo Planilha do Microsoft Excel (3).xlsx")
df['PROVEDOR NET MAIS LTDA'] = df['PROVEDOR NET MAIS LTDA'].apply(formatar_telefone)

# Inicializa o DataFrame anterior como vazio
df_anterior = pd.DataFrame()

while True:  # Loop infinito
    totalizacao_updates = []
    sleep(1.5)
    # Itera sobre os valores da coluna
    for index, row in df.iterrows():
        TEL = str(row['PROVEDOR NET MAIS LTDA'])  # Convertendo para string
        STATUS = row['STATUS']
        EMPRSA = row['EMPRESA']
        obs = row['TOTALIZAÇÃO']

        py.doubleClick(1254, 292)
        sleep(1)

        py.write(TEL)
        sleep(.80)
        # py.press('backspace')
        sleep(1)
        py.click(918, 680)
        sleep(5)
        py.click(380, 937)
        sleep(5)
        py.moveTo(503, 293)
        sleep(.5)
        py.mouseDown()
        sleep(.5)
        py.moveTo(1414, 305)
        py.mouseUp()
        sleep(4)
        py.hotkey('ctrl', 'c')
        msg = clipboard.paste()
        sleep(4)
        py.press('Esc')
        sleep(3)
        py.press('f5')
        sleep(5)
        texto = f'{msg} {EMPRSA}'
        df['TOTALIZAÇÃO'] = df['TOTALIZAÇÃO'].astype(str)
        print(texto)
        obs_formatado = textwrap.fill(texto)  # Formatar o texto adequadamente
        totalizacao_updates.append((index, obs_formatado))  # Armazenar o índice da linha e a observação formatada
        sleep(1)

        # Se o DataFrame anterior não está vazio e o valor de 'TOTALIZAÇÃO' mudou
        if not df_anterior.empty and df_anterior.at[index, 'TOTALIZAÇÃO'] != obs_formatado:
            enviar_email(obs_formatado)  # Chama a função enviar_email

    # Atualiza o DataFrame anterior com o atual
    df_anterior = df.copy()

    # Salvar o DataFrame no arquivo Excel
    with pd.ExcelWriter(r"C:\Users\Avantti\Desktop\Novo Planilha do Microsoft Excel (3).xlsx", engine='openpyxl', mode='a') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet3')  # Use um nome de planilha diferente

    print('Planilha salva')
    sleep(5)