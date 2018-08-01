## Assignment 5 Part 2
## Sadiq Abbas
## ITI 1120 Computing
## Graydon Hope 300045044

import math
class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'


class Rectangle:
    def __init__(self, point1, point2, colour):
        '''(Rectangle, Point, Point, String) -> None '''
        self.point1 = point1
        self.point2 = point2
        self.point1x = point1.x
        self.point1y = point1.y
        self.point2x = point2.x
        self.point2y = point2.y
        self.colour = colour

    def __repr__(self):
        '''(Rectangle) -> String '''
        return "Rectangle(" + str(self.point1) + ',' + str(self.point2) + ",'" + str(self.colour) + "')"

    def __str__(self):
        '''(Rectangle) -> String '''
        return "I am a " + str(self.colour) + " rectangle with bottom left corner at " + "(" + str(self.point1.x) +"," + str(self.point1.y) + ")" + " and top right corner at " + "(" + str(self.point2.x) + "," + str(self.point2.y) + ")"

    def __eq__(self, self2):
        '''(Rectangle, Rectangle) -> Bool'''
        return self.point1 == self2.point1 and self.point2 == self2.point2

    def move (self, dx, dy):
        '''(Rectangle, number, number) -> None'''
        self.point1.move(dx, dy)
        self.point2.move(dx, dy)

    def get_colour(self):
        '''(Rectangle) -> String '''
        return self.colour

    def reset_colour(self, newColour):
        '''(Rectangle, String) -> None'''
        self.colour = newColour

    def get_bottom_left(self):
        '''(Rectangle) -> Point '''
        return self.point1

    def get_top_right(self):
        '''(Rectangle) -> Point'''
        return self.point2

    def get_perimeter(self):
        '''(Rectangle) -> Number'''
        return ((2*(abs(self.point2x - self.point1x))) + (2*(abs(self.point2y - self.point1y))))

    def intersects(self, self2):
        '''(rectangle, rectangle) -> Bool '''
        if self.point1.x > self2.point2.x or self.point2.x < self2.point1.x or self.point2.y < self2.point1.y or self.point1.y > self2.point2.y:
            return False
        return True

    def get_area(self):
        '''(Rectangle) -> Number'''
        area = ((abs(self.point2x - self.point1x)) * (abs(self.point2y - self.point1y)))
        return area

    def contains(self, x, y):
        if self.point1.x > x or self.point2.x < x and self.point2.y < y or self.point1.y > y:
            return False
        return True

class Canvas:
    def __init__(self):
        '''(Canvas) -> None '''
        self.canvas = []

    def __len__(self):
        '''(Canvas) -> Int '''
        return len(self.canvas)

    def __repr__(self):
        '''(Canvas) -> String '''
        return str("Canvas(" + str(self.canvas) + ")")

    def add_one_rectangle(self, R2):
        '''(Canvas, Rectangle) -> None '''
        self.canvas.append(R2)

    def total_perimeter(self):
        '''(Canvas) -> Number'''
        total_P = 0
        for index in self.canvas:
            total_P = total_P + Rectangle.get_perimeter(index)
        return total_P

    def count_same_colour(self, colour):
        '''(Canvas, String) -> Int'''
        colour_count = 0
        for index in self.canvas:
            if index.colour == colour:
                colour_count += 1
        return colour_count

    def min_enclosing_rectangle(self):
        '''(Canvas) -> Rectangle '''
        min_x_coordinate = self.canvas[0].point1.x
        max_x_coordinate = self.canvas[0].point2.x
        min_y_coordinate = self.canvas[0].point1.y
        max_y_coordinate = self.canvas[0].point2.y
        for index in self.canvas[1:]:
            if min_x_coordinate > index.point1.x:
                min_x_coordinate = index.point1.x
            if max_y_coordinate < index.point2.y:
                max_y_coordinate = index.point2.y
            if max_x_coordinate < index.point2.x:
                max_x_coordinate = index.point2.x
            if min_y_coordinate > index.point1.y:
                min_y_coordinate = index.point1.y
            
        return Rectangle(Point(min_x_coordinate, min_y_coordinate),Point(max_x_coordinate, max_y_coordinate), "red")

    def common_point(self):
        '''(Canvas) -> Boolean '''
        for index in range(len(self.canvas)//2):
            for index2 in range(1,len(self.canvas)):
                if self.canvas[index].intersects(self.canvas[index2]) == False:
                    return False
        return True    
