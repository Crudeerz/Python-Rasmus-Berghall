from math import pi
from help_functions import check_int_float, circle_check_type_comparison, rectangle_check_type_comparison


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
        if circle_check_type_comparison(other) is False: return False
       
        if self.get_area == (other if type(other) in [int, float] else other.get_area): return True
        else: return False
       

       
    def __le__(self, other):
       if circle_check_type_comparison(other) is False: return False
       
       if self.get_area <= (other if type(other) in [int, float] else other.get_area): return True
       else: return False 


    def __ge__(self, other):
        if circle_check_type_comparison(other) is False: return False
       
        if self.get_area >= (other if type(other) in [int, float] else other.get_area): return True
        else: return False


    def __lt__(self, other):
       if circle_check_type_comparison(other) is False: return False
       
       if self.get_area < (other if type(other) in [int, float] else other.get_area): return True
       else: return False 


    def __gt__(self, other):
       if circle_check_type_comparison(other) is False: return False
       
       if self.get_area > (other if type(other) in [int, float] else other.get_area): return True
       else: return False


    @property
    def get_area(self):
        return self._radius **2 * pi

    @property
    def get_omkrets(self):
        return self._radius * 2 * pi 
    

    def translate(self, x, y):
        check_int_float(x, y)
        
        self._x = x
        self._y = y
    
    ## Kolla upp, denna funktion klarar ej alla punkter för en cirkel
    def is_inside(self, x, y):
        check_int_float(x, y)
        if ((self._x - self._radius) < x < float(self._x + self._radius)) and (float(self._y - self._radius) < y < float(self._y + self._radius)):     
            return True
        else: return False

    @property
    def is_unitcircle(self):
        if (self._x == 0 and self._y == 0) and (self._radius == 1):
            return True
        else: return False
        


    




class Rectangle:
    def __init__(self, x, y, side1, side2):
        check_int_float(x, y, side1, side2)
        self._x = x
        self._y = y
        self._side1 = side1
        self._side2 = side2

    def __repr__(self):
        return f"x = {self._x}, y = {self._y}, side1 = {self._side1}, side2 = {self._side2}"
    
    def __str__(self):
        return f"A rectangle with the middlepoint: {self._x}, {self._y} and the sides: {self._side1}, {self._side2}"

    def __eq__(self, other):
       if rectangle_check_type_comparison(other) is False: return False

       if self.get_area == (other if type(other) in [int, float] else other.get_area): return True
       else: return False

       
    def __le__(self, other):
       if rectangle_check_type_comparison(other) is False: return False
       
       if self.get_area <= (other if type(other) in [int, float] else other.get_area): return True
       else: return False 


    def __ge__(self, other):
        if rectangle_check_type_comparison(other) is False: return False
       
        if self.get_area >= (other if type(other) in [int, float] else other.get_area): return True
        else: return False


    def __lt__(self, other):
       if rectangle_check_type_comparison(other) is False: return False
       
       if self.get_area < (other if type(other) in [int, float] else other.get_area): return True
       else: return False 


    def __gt__(self, other):
       if rectangle_check_type_comparison(other) is False: return False
       
       if self.get_area > (other if type(other) in [int, float] else other.get_area): return True
       else: return False


    @property
    def get_area(self):
        return self._side1 * self._side2

    @property
    def get_omkrets(self):
        return self._side1 *2 + self._side2 *2
    

    def translate(self, x, y):
        check_int_float(x, y)
        
        self._x = x
        self._y = y
    
    def is_inside(self, x, y):
        check_int_float(x, y)
        if ((self._x - self._side1/2) < x < float(self._x + self._side1/2)) and (float(self._y - self._side2/2) < y < float(self._y + self._side2/2)):     
            return True
        else: return False
