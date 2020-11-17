import matplotlib.pyplot as pyplot
import FileIO


class Chart:
    def __init__(self):
        self.data = FileIO.FileIO()
        self.dataTable = self.data.dataTable

    def drawLineChart(self, x, y, title, xlabel, ylabel):
        pyplot.title(title)
        pyplot.ylabel(ylabel)
        pyplot.xlabel(xlabel)

        pyplot.plot(x, y, marker='o')
        pyplot.show()

    def drawBarChart(self, x, y, title, xlabel, ylabel):
        pyplot.title(title)
        pyplot.ylabel(ylabel)
        pyplot.xlabel(xlabel)

        pyplot.bar(x, y)
        pyplot.show()
