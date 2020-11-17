import FileIO
import Date


class TemperatureData:
    def __init__(self, x):
        self.fileData = FileIO.FileIO().dataTable
        self.date = Date.Date(x)
        self.minTemp = self.fileData[x, 3]
        self.maxTemp = self.fileData[x, 2]
        self.snowfall = self.fileData[x, 4]

