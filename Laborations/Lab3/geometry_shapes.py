from math import pi
from help_functions import check_int_float, circle_check_type_comparison


class Circle:
    
    def __init__(self, x, y, radius):
        check_int_float(x, y, radius)

        self._x = x
        self._y = y
        self._radius = radius

    def __repr__(self):
        return f"x = {self._x}, y = {self._y}, radius = {self._radius}"
    
    def __str__(self):
        return f"A circle with the middlepoint: {self._x}, {self._y} and the radius: {self._radius}"
    
    def __eq__(self, other):
    #    if type(other) not in [int, float, Circle]:
    #        raise ValueError(f"unsupported operand(s) for comparision with 'Circle' and {type(other)}, should be int or 'Circle")
       circle_check_type_comparison(other)

       if self._radius == (other if type(other) in [int, float] else other._radius): return True
       else: return False

       
    def __le__(self, other):
       if type(other) not in [int, float, Circle]:
           raise ValueError(f"unsupported operand(s) for comparision with 'Circle' and {type(other)}, should be int or 'Circle")
       
       if self._radius <= (other if type(other) in [int, float] else other._radius): return True
       else: return False 


    def __ge__(self, other):
       if type(other) not in [int, float, Circle]:
           raise ValueError(f"unsupported operand(s) for comparision with 'Circle' and {type(other)}, should be int or 'Circle")
       
       if self._radius >= (other if type(other) in [int, float] else other._radius): return True
       else: return False


    def __lt__(self, other):
       if type(other) not in [int, float, Circle]:
           raise ValueError(f"unsupported operand(s) for comparision with 'Circle' and {type(other)}, should be int or 'Circle")
       
       if self._radius < (other if type(other) in [int, float] else other._radius): return True
       else: return False 


    def __gt__(self, other):
       if type(other) not in [int, float, Circle]:
           raise ValueError(f"unsupported operand(s) for comparision with 'Circle' and {type(other)}, should be int or 'Circle")
       
       if self._radius > (other if type(other) in [int, float] else other._radius): return True
       else: return False


    @property
    def get_area(self):
        return f"{self._radius **2 * pi:.3f}"

    @property
    def get_omkrets(self):
        return f"{self._radius * 2 * pi:.3f}" 
    

    def translate(self, x, y):
        check_int_float(x, y)
        
        self._x = x
        self._y = y
    
    
    def is_inside(self, x, y):
        ...
        #check_numeric(x, y, message=f"unsupported type for translation from {type(self._x)} to {type(x)}, should be int or float.")

        # if  type(x) not in [float, int]:
        #     raise ValueError(f"unsupported type for translation from {type(self._x)} to {type(x)}, should be int or float.")
        # elif type(y) not in [float, int]:
        #     raise ValueError(f"unsupported type for translation from {type(self._y)} to {type(y)}, should be int or float.")


    


        

   





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


