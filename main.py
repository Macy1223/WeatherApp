from readapi_key import readapi_key
from api_connection import get_response
from Kalkulator import Conversion


def main():
    api_key = readapi_key("api_key.txt")
    response = get_response(api_key)
    convertion = Conversion(response)
    print(convertion.temp)
    convertion.kel_to_cel()
    print(convertion.temp)


if __name__ == '__main__':
    main()

