import TemperatureData
import FileIO


class WeatherAnalyzer:
    def __init__(self):
        self.dataTable = FileIO.FileIO().dataTable
        self.tempData = []
        for i in range(len(self.dataTable)):
            self.tempData.append(TemperatureData.TemperatureData(i))
