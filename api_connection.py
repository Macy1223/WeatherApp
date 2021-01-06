import requests


def get_response(api_key):
    '''

    :param api_key:
    :return: Response from weather api
    '''
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q=warsaw&appid={api_key.strip()}").json()
    return response

