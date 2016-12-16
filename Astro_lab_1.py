#Daniel Rono and Allison Watson.
#September 23, 2015.

import math
x1 = float (input("Please enter the lower limit of your integral: "))
x2 = float (input("Please enter the upper limit of your integral: "))

print (x1,x2)
ntrap = 5
deltax = (x2-x1)/ntrap
    

def f(x):
    y = math.sin (x)
    print ("The sine of x1 is ", y)
    return y

def trap (a,b):
    area = 0.5*(deltax)*(f(a)+f(b))
    return area

x=x1
areaT = 0

while x<=x2:
    areaT += trap (x, x+deltax)
    x += deltax

print ("The area is ", areaT)



    
    



