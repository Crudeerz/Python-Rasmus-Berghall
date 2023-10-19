from geometry_shapes import Circle, Rectangle, Cube, Sphere

# Test geometry shapes

# Initialize circles for tests
cirkel1 = Circle(1,3,3)
cirkel2 = Circle(1,1,3)
cirkel3 = Circle(1,1,2)
# Unitcircle
cirkel4 = Circle(0, 0, 1)




def test_circles():
    # Test comparison operators
    assert cirkel1==cirkel2
    assert cirkel1<=cirkel2
    assert cirkel1>=cirkel2
    assert cirkel1>cirkel3
    assert cirkel3<cirkel1
    # Test methods
    assert cirkel1.is_inside(1,2) == True
    assert cirkel1.is_inside(3,6) == False
    # Test properties
    assert cirkel4.is_unitcircle == True
    assert cirkel1.is_unitcircle == False
    assert cirkel1.get_area == 28.274333882308138
    assert  cirkel1.get_omkrets == 18.84955592153876



# Init rectangles for tests
rektangel1 = Rectangle(3, 4, 4, 5)
rektangel2 = Rectangle(2, 6, 5, 4)
rektangel3 = Rectangle(2, 4, 6, 3)
rektangel4 = Rectangle(3, 6, 3, 3)

def test_rectangles():
    # Test comparison operators
    assert rektangel1==rektangel2
    assert rektangel1<=rektangel2
    assert rektangel1>=rektangel2
    assert rektangel1>rektangel3
    assert rektangel3<rektangel1
    # Test methods
    assert rektangel3.is_inside(4,3) == True
    assert rektangel3.is_inside(4,7) == False
    # Test properties
    assert rektangel4.is_square == True
    assert rektangel3.is_square == False
    assert rektangel1.get_area == 20
    assert rektangel1.get_area != 30
    assert rektangel4.get_omkrets == 12



# Init cubes for tests
kub1 = Cube(3, 4, 2, 4)
kub2 = Cube(4, 2, 1, 4)
kub3 = Cube(4, 2, 6, 6)

def test_cubes():
    # Test comparison operators
    assert kub1==kub2
    assert kub1<=kub3
    assert kub1>=kub2
    assert kub3>kub1
    assert kub1<kub3
    # Test methods
    assert kub1.is_inside(3,4,2) == True
    assert kub1.is_inside(6,7,2) == False
    # Test properties
    assert kub1.get_volume == 64
    assert kub3.get_volume == 216
    assert kub2.get_volume != 200 
    


# Init spheres for tests
sfär1 = Sphere(3,4,6,3)
sfär2 = Sphere(3,4,6,4)
sfär3 = Sphere(4,2,6,4)

def test_spheres():
    # Test comparison operators
    assert sfär2==sfär3
    assert sfär2<=sfär3
    assert sfär2>=sfär1
    assert sfär3>sfär1
    assert sfär1<sfär3 
    # Test methods
    assert sfär3.is_inside(4,2,7) == True
    assert sfär3.is_inside(1,1,1) == False
    # Test properties
    assert sfär1.get_volume == 113.09733552923255






