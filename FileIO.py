import numpy as np


class FileIO:
    def __init__(self):
        self.filePath = 'weather.csv'
        self.dataTable = self.read_weather()
        self.y = self.dataTable[:, 3]
        self.x = self.dataTable[:, 1]

    def read_weather(self):
        # Read the csv file
        data = np.loadtxt(self.filePath, delimiter=',', skiprows=1, usecols=(0, 1, 2, 3, 4), dtype=np.float)

        return data
