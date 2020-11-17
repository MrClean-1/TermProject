import Date


class TemperatureData:
    def __init__(self, x, dataTable):
        self.date = Date.Date(x, dataTable)
        self.minTemp = dataTable[x, 3]
        self.maxTemp = dataTable[x, 2]
        self.snowfall = dataTable[x, 4]
