from math import sqrt, pi

## 1. define a class Point
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    ## 2. method calculate distance
    def distance(self, other_point):
        return sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)


## 3. circle
class Circle():
    def __init__(self, point, r):
        self.center = point
        self.radius = r

    def area(self):
        return pi * self.radius ** 2

    ## 4. add a contains() method:
    def contains(self, point):
        if point.distance(self.center) < self.radius:
            return True
        else:
            return False

## 5. rectangle
class Rectangle():
    def __init__(self, bottomleft, width, height):
        self.bottomleft = bottomleft
        self.width = width
        self.height = height


    def area(self):
        return self.width*self.height

    ## 6. contains a point
    def contains(self, point):
        if (point.x > self.bottomleft.x) and (point.x < self.bottomleft.x + self.width):
            if (point.y > self.bottomleft.y) and (point.y < self.bottomleft.y + self.height):
                return True
            else:
                return False
        else:
            return False

## 7. square as subset of rectangle
class Square(Rectangle):
    def __init__(self, bottomleft, side):
        self.bottomleft = bottomleft
        self.width = side
        self.height = side



