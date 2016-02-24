#program to print a circle in python
#creds to Tycho for idea behind print_circle()
#2nd algorithm appears to be faster by some unknown factor judging from tests...
import sys
import math
import time
radius = 15
min_radius=12

def circle():
    result = ""
    for i in range(-radius, radius):
        for j in range(-radius, radius):
            if (i*i+j*j < radius*radius and i*i+j*j > min_radius*min_radius):
                result+='*'
            else:
                result+=' '
        result+='\n'
    return result

#Note that the first algorithm checks for POINT inclusion (whether if point is in circle or not) whereas 2nd checks for if specific length is > 0. They are semantically different.

def circle_new():
    result = ""
    for i in range(-radius, radius):
        start = radius-(radius*radius-(i)**2)**(0.5)
        spaces = " "*int(start)
        height = 0-i
        if height < 0: height = -height
        outer_end = min_radius - height
        if outer_end>0:
            outer_end = radius-(min_radius**2-height**2)**(0.5)
        elif outer_end == 0:
            outer_end = radius-(min_radius**2-height**2)**(0.5)-0.1
        else:
            outer_end = 0
        numstars = int(outer_end-int(start)-0.01)
        stars="*"*numstars
        gap = " "*int(2*(radius - numstars - int(start))-1)
        if outer_end == 0:
            stars="*"*(int(2*(radius - int(start))-1))
            result+= " "+spaces+stars+"\n"
        else:
            result+= " "+spaces+stars+gap+stars+"\n"
    return result

start = time.time()
result=circle()
##print result
end = time.time()
print end - start

start = time.time()
result=circle_new()
##print result
end = time.time()
print end - start
