import requests


def obter_operadora(numero_telefone):
    """
    Consulta a operadora de um número de telefone utilizando a API da Anatel.

    Args:
        numero_telefone (str): Número de telefone no formato com DDD (ex: 61987654321).

    Returns:
        str: Nome da operadora, se encontrada.
        None: Caso haja erro na consulta.
    """
    url = f"https://apps.anatel.gov.br/ComparadorOperadora/Consultar?numero={numero_telefone}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve erro na requisição

        dados = response.json()  # Converte a resposta para JSON
        operadora = dados.get('operadora')
        return operadora

    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP ao consultar o número {numero_telefone}: {http_err}")
        return None

    except Exception as err:
        print(f"Erro geral ao consultar o número {numero_telefone}: {err}")
        return None


# Exemplo de uso
if __name__ == "__main__":
    numero = "82999020822"
    operadora = obter_operadora(numero)

    if operadora:
        print(f"A operadora do número {numero} é {operadora}")
    else:
        print(f"Não foi possível obter a operadora do número {numero}")