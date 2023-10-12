
def check_int_float(x = None, y = None, z = None, c = None):
     '''
     Checks if parameters passed to function is float or integer.

                Parameters: 
                            x (int/float): Default = None
                            y (int/float): Default = None
                            z (int/float): Default = None
                            c (int/float): Default = None

                Returns: 
                            Raises ValueError if any parameter is not int, float or None

     '''
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

# def circle_check_type_comparison(other):
#      '''
#      Checks if 'circle' comparison parameter is applicable for comparison.
#      Returns False instead of raising error to match example code in lab3 

#                 Parameters: 
#                             Required: other (int/float,obj)

#                 Returns: 
#                             False
#      ''' 
#      from geometry_shapes import Circle

#      # returning False instead of raising error to match output in code example from laboration
#      if type(other) not in [int, float, Circle]:
#         return False
    
def check_type_comparison(other, class_name):
     '''
     Checks if 'other' comparison parameter is applicable for comparison.
     Returns False instead of raising error to match example code in lab3 

                Parameters: 
                            Required: other (int/float,obj)

                Returns: 
                            False
     '''
     if type(other) not in [int, float, class_name]:
           return False