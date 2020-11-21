class Point:
    #static property
    points = 0
    @staticmethod # belongs to the class, not to the instance
    def how_many_points():
        return Point.points

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        Point.points += 1
    
    def where_am_i(self):
        return(f'Point at {self.x}, {self.y}')

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy


if __name__ == '__main__':

    p1 = Point(5, 7)
    p2 = Point(15, 17)
    p3 = Point(25, 27)
    p1.move_by(1, 1)
    print(Point.how_many_points())
    p1.where_am_i()