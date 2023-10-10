from geometry_shapes import Circle, Rectangle

cirkel1 = Circle(1,3,3)

cirkel2 = Circle(1,1,3)

cirkel3 = Circle(1,1,2)

cirkel4 = Circle(1, 4.0, 3)


# print(cirkel1.is_inside(3.5, 0.5))
# print(cirkel1)

rektangel1 = Rectangle(3, 4, 4, 5)
rektangel2 = Rectangle(2, 6, 4, 4)
# print(cirkel1>=rektangel1)

print(rektangel1.get_area)
print(rektangel1==cirkel1)
