import matplotlib.pyplot as pyplot
import FileIO


class Chart:
    def __init__(self):
        self.data = FileIO.FileIO()
        self.dataTable = self.data.dataTable

    def drawLineChart(self, x, y):
        pyplot.title('Temperatures in Calgary between Jan-Dec in 2000')
        pyplot.ylabel('Min Temperatures (F)')
        pyplot.xlabel("Month of Year")

        pyplot.plot(x, y, marker='o')
        pyplot.show()

    def drawBarChart(self, x, y):
        pyplot.title('Temperatures in Calgary between Jan-Dec in 2000')
        pyplot.ylabel('Min Temperatures (F)')
        pyplot.xlabel("Month of Year")

        pyplot.bar(x, y)
        pyplot.show()
