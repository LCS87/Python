import phonenumbers
import requests

# Ajuste o telefone para usar a biblioteca
telefone = "+558294237926"
telefone_ajustado = phonenumbers.parse(telefone)

# Descobrir a localização do telefone
from phonenumbers import geocoder
local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
print(f"Localização: {local}")

# Obter informações básicas do número de telefone
numero_info = phonenumbers.parse(telefone, None)

# Obter a operadora do telefone usando o serviço numverify.com
api_key = 'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'
url = f"http://apilayer.net/api/validate?access_key={api_key}&number={telefone}&country_code=&format=1"
response = requests.get(url)
data = response.json()

# Verificar se há erros na resposta da API
if 'error' in data:
    print(f"Erro ao obter informações do número: {data['error']['info']}")
else:
    operadora = data.get('carrier', 'Operadora não disponível')
    print(f"Operadora: {operadora}")