import matplotlib.pyplot as pyplot
pyplot.rcParams['toolbar'] = 'None'

size_x = 4
size_y = 4
pyplot.axis('off')

def line(x1, y1, x2, y2):
    pyplot.plot([x1, x2], [y1, y2], color='black')


def clearLine(x1, y1, x2, y2):
    pyplot.plot([x1, x2], [y1, y2], color='white')


def drawMazeBorder():
  line(0, 0, size_x, 0)
  line(0, 0, 0, size_y)
  line(size_x, 0, size_x, size_y)
  line(0, size_y, size_x, size_y)


drawMazeBorder()
pyplot.show()