import matplotlib.pyplot as pyplot
from Cell import Cell

pyplot.rcParams['toolbar'] = 'None'

size_x = 4
size_y = 4
pyplot.axis('off')
maze = []


def line(x1, y1, x2, y2):
    pyplot.plot([x1, x2], [y1, y2], color='black')


def clear_lower_wall(x, y):
    pyplot.plot([x, x+1], [y, y], color='white')
    for cell in maze:
        if cell.origin[0] == x and cell.origin[1] == y - 1:
            cell.existsUpperWall = False


def clear_upper_wall(x, y):
    pyplot.plot([x, x+1], [y+1, y+1], color='white')
    for cell in maze:
        if cell.origin[0] == x and cell.origin[1] == y + 1:
            cell.existsLowerWall = False


def clear_left_wall(x, y):
    pyplot.plot([x, x], [y, y+1], color='white')
    for cell in maze:
        if cell.origin[0] == x - 1 and cell.origin[1] == y:
            cell.existsRightWall = False


def clear_right_wall(x, y):
    pyplot.plot([x + 1, x + 1], [y, y + 1], color='white')
    for cell in maze:
        if cell.origin[0] == x + 1 and cell.origin[1] == y:
            cell.existsLeftWall = False


def draw_cells():
    for x in range(size_x):
        for y in range(size_y):

            cell = Cell(x, y)
            cell.existsRightWall = True
            cell.existsLeftWall = True
            cell.existsLowerWall = True
            cell.existsUpperWall = True
            cell.origin = (x, y)

            line(x, y, x + 1, y)
            line(x, y + 1, x + 1, y + 1)
            line(x, y, x, y + 1)
            line(x + 1, y, x + 1, y + 1)

            maze.append(cell)


draw_cells()
pyplot.show()


