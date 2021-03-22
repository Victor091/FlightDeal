import pandas as pd


class DataManager:

    def __init__(self):
        data = pd.read_csv('data/Flight Deals.csv')
        self.to_IATA_City = self.separateCityByComma(data['IATA Code'].to_list())
        self.information = data.to_dict(orient='records')

    def separateCityByComma(self, cities: list):
        all_cities = ""

        for IATA_city in cities:
            all_cities += IATA_city + ','

        return all_cities[:-1]
