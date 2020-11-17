import FileIO


class Date:
    def __init__(self, x):
        self.dataTable = FileIO.FileIO().dataTable
        self.month = self.dataTable[x, 1]
        self.year = self.dataTable[x, 0]
