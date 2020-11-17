import numpy as np


class FileIO:
    def __init__(self):
        self.filePath = ''
        self.dataTable = ''
        self.data = self.read_weather()

    def read_weather(self):
        # Read the csv file
        data = np.loadtxt(self.filePath, delimiter=',', skiprows=1, usecols=(0, 1, 2, 3, 4), dtype=np.float)

        return data


