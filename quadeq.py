#program that solves the quadratic equations

import cmath


#what are the variables
a = float(input("what is your A value:"))
b = float(input("What is your B value:"))
c = float(input("What is your C value:"))

#calculate
disc = (b**2) - (4*a*c)

x_val1 = (-b + cmath.sqrt(disc)

x_val2 = (-b - cmath.sqrt(disc))//(2*a)

print ("x = ", x_val1)

print ("x = ", x_val2)