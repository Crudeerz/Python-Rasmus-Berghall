

def check_int_float(x = None, y = None, z = None, c = None):
     if x is not None:
        if type(x) not in [float, int]:
            raise ValueError(f"unsupported type for '{x}' : {type(x)}, should be int or float")
     if y is not None:
        if type(y) not in [float, int]:
            raise ValueError(f"unsupported type for '{y}' : {type(y)}, should be int or float")
     if z is not None:   
        if type(z) not in [float, int]:
            raise ValueError(f"unsupported type for '{z}' : {type(z)}, should be int or float")
     if c is not None:   
        if type(c) not in [float, int]:
            raise ValueError(f"unsupported type for '{c}' : {type(c)}, should be int or float")

def circle_check_type_comparison(other):

    if type(other) not in [int, float, Circle]:
           raise ValueError(f"unsupported operand(s) for comparision with {type(other)}")
    
def rectangle_check_type_comparison(other):

    if type(other) not in [int, float, Rectangle]:
           raise ValueError(f"unsupported operand(s) for comparision with {type(other)}")
