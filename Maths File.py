#Maths File
#Pythagorean Theorum
rooted=0
import math
def pythag():
    length1=float(input("Please enter the length of one of the sides of the triangle that isn't the hypotenuse: "))
    length2=float(input("Please enter the length of the other side of the triangle that isn't the hypotenuse: "))
    squared=length1**2 + length2**2
    rooted= math.sqrt(squared)
    print (rooted, "is the length of the hypotenuse")
pythag()
    