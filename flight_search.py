import requests
import os

TEQUILA_FLY_ENDPOINT='https://tequila-api.kiwi.com/v2/search'
API_KEY = os.environ['TEQUILA_API_KEY']

HEADERS = {
    'apikey': API_KEY
}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def search_Flight(self, information_fly: dict):

        response = requests.get(url=TEQUILA_FLY_ENDPOINT, params=information_fly, headers=HEADERS)
        response.raise_for_status()

        data = response.json()
        for fly in range(len(data["data"])):
            print(f'From: {data["data"][fly]["countryFrom"]} \n'
                  f'To: {data["data"][fly]["cityTo"]} \n'
                  f'Price: {data["data"][fly]["deep_link"]}\n\n')
