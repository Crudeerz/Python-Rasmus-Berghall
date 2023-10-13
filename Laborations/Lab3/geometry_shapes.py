from math import pi, sqrt
from help_functions import check_int_float, check_type_comparison


class Circle:
    '''
    Class for Circle-object

    When initializing a Circle you should enter the circles middlepoint in a 2d coordinate system
    and the length of the sides.

    When using any comparing operator for the Circle we are comparing area and ignoring the middlepoint (x,y)

                Parameters
                            x:       (int/float)
                            y:       (int/float)
                            radius:  (int/float)
    
    '''
    
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
        if check_type_comparison(other, Circle) is False: return False
       
        if self.get_area == (other if type(other) in [int, float] else other.get_area): return True
        else: return False
       

       
    def __le__(self, other):
       if check_type_comparison(other, Circle) is False: return False
       
       if self.get_area <= (other if type(other) in [int, float] else other.get_area): return True
       else: return False 


    def __ge__(self, other):
        if check_type_comparison(other, Circle) is False: return False
       
        if self.get_area >= (other if type(other) in [int, float] else other.get_area): return True
        else: return False


    def __lt__(self, other):
       if check_type_comparison(other, Circle) is False: return False
       
       if self.get_area < (other if type(other) in [int, float] else other.get_area): return True
       else: return False 


    def __gt__(self, other):
       if check_type_comparison(other, Circle) is False: return False
       
       if self.get_area > (other if type(other) in [int, float] else other.get_area): return True
       else: return False


    @property
    def get_area(self):
        return self._radius **2 * pi

    @property
    def get_omkrets(self):
        return self._radius * 2 * pi 
    
    @property
    def is_unitcircle(self):
        if self._x == 0 and self._y == 0 and self._radius == 1:
            return True
        else: return False

    def translate(self, x, y):
        check_int_float(x, y)
        
        self._x = x
        self._y = y
    
    def is_inside(self, x, y):
        check_int_float(x, y)

        # Beräkna distancen mellan punkterna och jämför med radien
        # för att se om punkten är i cirkeln
        dist = sqrt((self._x - x)**2 + (self._y - y)**2)

        return True if dist < self._radius else False
        


        


class Rectangle:
    '''
    Class for Rectangle-object

    When initializing a Rectangle you should enter the rectangles middlepoint in a 2d coordinate system
    and the length of the sides.

    When using any comparing operator for the Rectangle we are comparing area and ignoring the middlepoint (x,y)

                Parameters
                            x:       (int/float)
                            y:       (int/float)
                            side1:    (int/float)
                            side2:    (int/float)
    
    '''
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
       if check_type_comparison(other, Rectangle) is False: return False

       if self.get_area == (other if type(other) in [int, float] else other.get_area): return True
       else: return False

       
    def __le__(self, other):
       if check_type_comparison(other, Rectangle) is False: return False
       
       if self.get_area <= (other if type(other) in [int, float] else other.get_area): return True
       else: return False 


    def __ge__(self, other):
        if check_type_comparison(other, Rectangle) is False: return False
       
        if self.get_area >= (other if type(other) in [int, float] else other.get_area): return True
        else: return False


    def __lt__(self, other):
       if check_type_comparison(other, Rectangle) is False: return False
       
       if self.get_area < (other if type(other) in [int, float] else other.get_area): return True
       else: return False 


    def __gt__(self, other):
       if check_type_comparison(other, Rectangle) is False: return False
       
       if self.get_area > (other if type(other) in [int, float] else other.get_area): return True
       else: return False


    @property
    def get_area(self):
        return self._side1 * self._side2

    @property
    def get_omkrets(self):
        return self._side1 *2 + self._side2 *2
    
    @property
    def is_square(self):
        return True if self._side1 == self._side2 else False    

    def translate(self, x, y):
        check_int_float(x, y)
        
        self._x = x
        self._y = y
    
    def is_inside(self, x, y):
        check_int_float(x, y)

        # Kolla om punkten ligger innanför instansen för objektet
        if (((self._x - self._side1/2) < x < (self._x + self._side1/2)) and
            ((self._y - self._side2/2) < y < (self._y + self._side2/2))): 
            return True  
        else: return False


class Cube:
    '''
    Class for Cube-object

    When initializing a Cube you should enter the cubes middlepoint in a 3d coordinate system
    and the length of the sides.

    When using any comparing operator for the Cube we are comparing volume and ignoring the middlepoint (x,y,z)

                Parameters
                            x:       (int/float)
                            y:       (int/float)
                            z:       (int/float)
                            side:    (int/float)
    
    '''
    def __init__(self, x, y, z, side):
        check_int_float(x, y, z, side)
        self._x = x
        self._y = y
        self._z = z
        self._side = side

    def __repr__(self):
        return f"x = {self._x}, y = {self._y}, z = {self._z}, side = {self._side}"
    
    def __str__(self):
        return f"A cube with the middlepoint: {self._x}, {self._y}, {self._z} and the sides: {self._side}"

    def __eq__(self, other):
       if check_type_comparison(other, Cube) is False: return False

       if self.get_volume == (other if type(other) in [int, float] else other.get_volume): return True
       else: return False

       
    def __le__(self, other):
       if check_type_comparison(other, Cube) is False: return False
       
       if self.get_volume <= (other if type(other) in [int, float] else other.get_volume): return True
       else: return False 


    def __ge__(self, other):
        if check_type_comparison(other, Cube) is False: return False
       
        if self.get_volume >= (other if type(other) in [int, float] else other.get_volume): return True
        else: return False


    def __lt__(self, other):
       if check_type_comparison(other, Cube) is False: return False
       
       if self.get_volume < (other if type(other) in [int, float] else other.get_volume): return True
       else: return False 


    def __gt__(self, other):
       if check_type_comparison(other, Cube) is False: return False
       
       if self.get_volume > (other if type(other) in [int, float] else other.get_volume): return True
       else: return False


    @property
    def get_volume(self):
        return self._side ** 3
 

    def translate(self, x, y, z):
        check_int_float(x, y, z)
        
        self._x = x
        self._y = y
        self._z = z
    
    def is_inside(self, x, y, z):
        check_int_float(x, y, z)

        # Kolla om punkten ligger innanför instansen för objektet
        if  (((self._x - self._side/2) < x < (self._x + self._side/2)) and 
             ((self._y - self._side/2) < y < (self._y + self._side/2)) and
             ((self._z - self._side/2) < z < (self._z + self._side/2))): 
            return True  
        else: return False


class Sphere:
    '''
    Class for Sphere-object

    When initializing a Sphere you should enter the spheres middlepoint in a 3d coordinate system
    and the radius af the spere.

    When using any comparing operator for the Sphere we are comparing volume and ignoring the middlepoint (x,y,z)

                Parameters
                            x:       (int/float)
                            y:       (int/float)
                            z:       (int/float)
                            radius:    (int/float)
    
    '''
    def __init__(self, x, y, z, radius):
        check_int_float(x, y, z, radius)
        self._x = x
        self._y = y
        self._z = z
        self._radius = radius

    def __repr__(self):
        return f"x = {self._x}, y = {self._y}, z = {self._z}, radius = {self._radius}"
    
    def __str__(self):
        return f"A sphere with the middlepoint: {self._x}, {self._y}, {self._z} and the radius: {self._radius}"

    def __eq__(self, other):
       if check_type_comparison(other, Sphere) is False: return False

       if self.get_volume == (other if type(other) in [int, float] else other.get_volume): return True
       else: return False

       
    def __le__(self, other):
       if check_type_comparison(other, Sphere) is False: return False
       
       if self.get_volume <= (other if type(other) in [int, float] else other.get_volume): return True
       else: return False 


    def __ge__(self, other):
        if check_type_comparison(other, Sphere) is False: return False
       
        if self.get_volume >= (other if type(other) in [int, float] else other.get_volume): return True
        else: return False


    def __lt__(self, other):
       if check_type_comparison(other, Sphere) is False: return False
       
       if self.get_volume < (other if type(other) in [int, float] else other.get_volume): return True
       else: return False 


    def __gt__(self, other):
       if check_type_comparison(other, Sphere) is False: return False
       
       if self.get_volume > (other if type(other) in [int, float] else other.get_volume): return True
       else: return False


    @property
    def get_volume(self):
        return (4 * pi * self._radius**3) / 3
 

    def translate(self, x, y, z):
        check_int_float(x, y, z)
        
        self._x = x
        self._y = y
        self._z = z
    
    def is_inside(self, x, y, z):
        check_int_float(x, y, z)

        # Beräkna distancen mellan punkterna och jämför med radien
        # för att se om punkten är i cirkeln
        dist = sqrt((self._x - x)**2 + (self._y - y)**2 + (self._z -z)**2)
        return True if dist < self._radius else False
        
        