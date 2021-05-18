# Make a program that reads three floating point values: A, B and C. Then, calculate and show:
# a) the area of the rectangled triangle that has base A and height C.
# b) the area of the radius's circle C. (pi = 3.14159)
# c) the area of the trapezium which has A and B by base, and C by height.
# d) the area of ​​the square that has side B.
# e) the area of the rectangle that has sides A and B.

# Input
# The input file contains three double values with one digit after the decimal point.

# Output
# The output file must contain 5 lines of data. Each line corresponds to one of the areas described above, always with a corresponding message (in Portuguese) and one space between the two points and the value. The value calculated must be presented with 3 digits after the decimal point.

a, b, c = (input().split(' '))

a = float(a)
b = float(b)
c = float(c)

triangle = ((a*c)/2)
circle = (3.14159 * (c**2))
trapezium = (((a + b)*c)/2)
square = (b * b)
rectangle = (a * b)

print('''TRIANGULO: {:.3f} \n 
CIRCULO: {:.3f} \n 
TRAPEZIO: {:.3f} \n 
QUADRADO: {:.3f} \n 
RETANGULO: {:.3f} \n '''.format(triangle, circle, trapezium, square, rectangle))