from geometry_shapes import Circle, Rectangle, Cube, Sphere

cirkel1 = Circle(1,3,3)

cirkel2 = Circle(1,1,3)

cirkel3 = Circle(1,1,2)

cirkel4 = Circle(0, 0, 1)

rektangel1 = Rectangle(3, 4, 4, 5)

rektangel2 = Rectangle(2, 6, 5, 5)

kub1 = Cube(3, 4, 2, 4)

kub2 = Cube(4, 2, 1, 4)

sfär1 = Sphere(3,4,6,3)

sfär2 = Sphere(3,4,6,4)

# print(cirkel1.is_unitcircle)
# print(cirkel4.is_unitcircle)
# print(rektangel1.is_square)
# print(rektangel2.is_square)

# print(kub1.is_inside(4,5,3))

print(sfär1.is_inside(2, 3, 3))





