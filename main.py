#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime
from dateutil.relativedelta import relativedelta

flight_search = FlightSearch()
data_manager = DataManager()


date_now = datetime.now().strftime('%d/%m/%Y')
date_six_months_later = (datetime.now() + relativedelta(months=6)).strftime('%d/%m/%Y')

print(data_manager.to_IATA_City)


params = {
    'fly_from': 'MEX',
    'fly_to': data_manager.to_IATA_City,
    'date_from': date_now,
    'date_to': date_six_months_later
}

flight_search.search_Flight(params)

