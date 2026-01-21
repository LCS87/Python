import requests

def obter_score_cpf(cpf, client_id, client_secret):
    # URL da API da Serasa (exemplo fictício)
    url_token = "https://api.serasa.com/oauth2/token"
    url_score = f"https://api.serasa.com/credit-score/v1/{cpf}"

    # Autenticação para obter o token de acesso
    auth_response = requests.post(url_token, data={
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    })

    if auth_response.status_code == 200:
        token = auth_response.json().get('access_token')
    else:
        return f"Erro ao obter token: {auth_response.json()}"

    # Consulta do score utilizando o token de acesso
    headers = {
        'Authorization': f'Bearer {token}'
    }
    score_response = requests.get(url_score, headers=headers)

    if score_response.status_code == 200:
        return score_response.json()
    else:
        return f"Erro ao obter score: {score_response.json()}"

# Exemplo de uso
client_id = 'SEU_CLIENT_ID'
client_secret = 'SEU_CLIENT_SECRET'
cpf = '11394794401'  # CPF de exemplo

score_info = obter_score_cpf(cpf, client_id, client_secret)
print(score_info)