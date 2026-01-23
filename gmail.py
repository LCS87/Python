import smtplib
import gmail.message

def enviar_email(CNPJ, MSG):
    corpo_email = """
    <p>MAQUINA FORA DE COMBATE!</p>
    <p></p>
    """

    msg = email.message.Message()
    msg['Subject'] = f"{CNPJ}, {MSG}"
    msg['From'] = 'wilgneroliveirawil@gmail.com'
    msg['To'] = 'wilgneroliveirawil@gmail.com'
    password = 'yqtv beau rwhv nfhf'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')