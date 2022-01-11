import requests
from main import Temperatures
import unittest


class TestTemperaturesModel(unittest.TestCase):
    def setUp(self):
        self.temps = requests.post("https://tues2022.proxy.beeceptor.com/my/api/test").json()

    def tearDown(self):
        pass

    def test_highestTemperature(self):
        temperatures = []
        for i in range(0, 5):
            temperatures.append(self.temps['data'][i]['temperature'])
        list.sort(temperatures, reverse=True)
        val = Temperatures.highestTemperature()
        assert val == temperatures[0]

    def test_lowestTemperature(self):
        temperatures = []
        for i in range(0, 5):
            temperatures.append(self.temps['data'][i]['temperature'])
        list.sort(temperatures)
        val = Temperatures.lowestTemperature()
        assert val == temperatures[0]
    
    def test_midTemperature(self):
        mid = 0
        for i in range(0, 5):
            mid += float(self.temps['data'][i]['temperature'])
        mid /= 5
        val = Temperatures.midTemperature()
        assert val == mid

if __name__ == '__main__':
    unittest.main()