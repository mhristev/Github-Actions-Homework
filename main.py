import requests

TEMPERATURES_URL = "https://tues2022.proxy.beeceptor.com/my/api/test"

class Temperatures:
    @staticmethod
    def highestTemperature():
        data = requests.post(TEMPERATURES_URL).json()
   
        temperatures = []
        for i in range(0, 5):
            temperatures.append(data['data'][i]['temperature'])
        list.sort(temperatures, reverse=True)
        return temperatures[0]

    @staticmethod
    def lowestTemperature():
        data = requests.post(TEMPERATURES_URL).json()
        temperatures = []
        for i in range(0, 5):
            temperatures.append(data['data'][i]['temperature'])
        list.sort(temperatures)
        return temperatures[0]

    @staticmethod
    def midTemperature():
        data = requests.post(TEMPERATURES_URL).json()
        mid = 0
        for i in range(0, 5):
            mid += float(data['data'][i]['temperature'])
        mid /= 5
        return mid





