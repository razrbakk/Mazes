#
# (x, y+1)  ************ (x+1, y+1)
#           *          *
#           *          *
#           *          *
#   (x,y)   ************ (x+1,y)
#
#           Cell is always defined from lower left corner (x,y)
#


class Cell:
    existsRightWall = False
    existsLeftWall = False
    existsUpperWall = False
    existsLowerWall = False
    origin = ()

    def __init__(self, x, y):
        self.origin = (x, y)
