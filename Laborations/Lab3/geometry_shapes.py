from math import pi

class Circle:
    
    def __init__(self, x, y, radius):
        if type(x) not in [float, int]:
            raise ValueError("Please enter a numeric(float, int) value for x")
        elif type(y) not in [float, int]:
            raise ValueError("Please enter a numeric(float, int) value for y")
        elif type(radius) not in [float, int]:
            raise ValueError("Please enter a numeric(float, int) value for radius")

        self._x = x
        self._y = y
        self._radius = radius

    def __repr__(self):
        return f"x = {self._x}, y = {self._y}, radius = {self._radius}"
    
    def __str__(self):
        return f"A circel with the middlepoint: {self._x}, {self._y} with the radius: {self._radius}"
    
    def __eq__(self, other):
       if type(other) not in [int, float, Circle]:
           raise ValueError(f"unsupported operand(s) for comparision with 'Circle' and {type(other)}, should be int or 'Circle")
       
       if self._radius == (other if type(other) in [int, float] else other._radius): return True
       else: return False

#other if type(other) in [int, float] else
       
    def __le__(self, other):
       if type(other) not in [int, Circle]:
           raise ValueError(f"unsupported operand(s) for comparision with 'Circle' and {type(other)}, should be int or 'Circle")
       
       if self._radius <= (other if type(other) == int else other._radius): return True
       else: return False 


    def __ge__(self, other):
       if type(other) not in [int, Circle]:
           raise ValueError(f"unsupported operand(s) for comparision with 'Circle' and {type(other)}, should be int or 'Circle")
       
       if self._radius >= other._radius: return True
       else: return False


    def __lt__(self, other):
       if type(other) not in [int, Circle]:
           raise ValueError(f"unsupported operand(s) for comparision with 'Circle' and {type(other)}, should be int or 'Circle")
       
       if self._radius < other._radius: return True
       else: return False 


    def __gt__(self, other):
       if type(other) not in [int, Circle]:
           raise ValueError(f"unsupported operand(s) for comparision with 'Circle' and {type(other)}, should be int or 'Circle")
       
       if self._radius > other._radius: return True
       else: return False


    @property
    def get_area(self):
        return self._radius **2 * pi

    @property
    def get_omkrets(self):
        return self._radius * 2 * pi 
    

    


        

   





class Rectangle:
    def __init__(self, x, y, side1, side2):
        self._x = x
        self._y = y
        self._side1 = side1
        self._side2 = side2

    def __repr__(self):
        return f"x = {self._x}, y = {self._y}, side1 = {self._side1}, side2 = {self._side2}"
    
    def __str__(self):
        return f"A rectangle with the middlepoint: {self._x}, {self._y} with the sides: {self._side1}, {self._side2}"


