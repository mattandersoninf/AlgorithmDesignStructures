# python impolementation of a point
# a point in 2-D Euclidean space which should contain the following
# - x-coordinate
# - y-coordinate
# - moveTo(new_x,new_y): changes the coordinates to be equal to the new coordinates
# - distanceTo(x_val,y_val): this function returns the distance from the current point to some other point as a float 

class Point:

    def __init__(self,x,y):
        self._x = x
        self._y = y

    @property
    def x(self):
        print("get x-coordinate")
        return self._x

    @x.setter
    def x(self,val):
        print("set x-coordinate")
        self._x = val

    @property
    def y(self):
        print("get y-coordinate")
        return self._x

    @y.setter
    def y(self,val):
        print("set y-coordinate")
        self._x = val

    @property
    def coordinates(self):
        print("get coordinates")
        return (self._x,self._y)

    def moveTo(self,new_x,new_y):
        self._x = new_x
        self._y = new_y

    def distanceTo(self,x_val,y_val):
        return ((self._x-x_val)**2+(self._y-y_val)**2)**.5
        