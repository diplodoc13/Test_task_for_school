'''
В функцию передаются координаты двух противоположных вершин одного прямоугольника
и двух противоположных вершин второго прямоугольника.
Найти, пересекаются ли эти прямоугольники?

def task(x1,y1,x2,y2,x3,y3,x4,y4):
    pass

print(task(1,1,2,2,3,3,4,4))
# >> OUT: False

'''


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.dot_1 = (min(x1, x2), min(y1, y2))
        self.dot_2 = (max(x1, x2), max(y1, y2))

    def __str__(self):
        return f'Rectangle: {self.dot_1} {self.dot_2}'

    def __repr__(self):
        return f'Rectangle({self.dot_1}, {self.dot_2})'

    def __eq__(self, other):
        return self.dot_1 == other.dot_1 and self.dot_2 == other.dot_2


def intersection(rect_1, rect_2):
    if rect_1.dot_1[0] > rect_2.dot_2[0] or rect_1.dot_2[0] < rect_2.dot_1[0]:
        return False
    if rect_1.dot_1[1] > rect_2.dot_2[1] or rect_1.dot_2[1] < rect_2.dot_1[1]:
        return False
    return True


def square_intersection(rect_1, rect_2):
    d_1 = (max(rect_1.dot_1[0], rect_2.dot_1[0]),
           max(rect_1.dot_1[1], rect_2.dot_1[1]))
    d_2 = (min(rect_1.dot_2[0], rect_2.dot_2[0]),
           min(rect_1.dot_2[1], rect_2.dot_2[1]))
    return (d_2[0] - d_1[0]) * (d_2[1] - d_1[1])


def square_rectangle(rect):
    return (rect.dot_2[0] - rect.dot_1[0]) * (rect.dot_2[1] - rect.dot_1[1])

def task(x1, y1, x2, y2, x3, y3, x4, y4):
    rect_1 = Rectangle(x1, y1, x2, y2)
    rect_2 = Rectangle(x3, y3, x4, y4)
    if square_rectangle(rect_1) == 0 or square_rectangle(rect_2) == 0:
        raise ValueError('We can`t compare rectangles with zero area') 

    if intersection(rect_1, rect_2):
        square_intersect = square_intersection(rect_1, rect_2)
        return f'Rectangles intersect. Square of intersection: {square_intersect}'
    else:
        return 'Rectangles do not intersect'

print(task(1, 1, 2, 2, 3, 3, 4, 4))