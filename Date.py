class Date:
    def __init__(self, x, dataTable):
        self.month = dataTable[x, 1]
        self.year = dataTable[x, 0]
