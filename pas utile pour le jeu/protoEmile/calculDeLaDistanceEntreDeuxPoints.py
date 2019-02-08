from math import *
def calculNorme(x1,y1,x2,y2):
    x=x2-x1
    y=y2-y1
    return sqrt(x*x+y*y)



print(calculNorme(0,10,20,10))
print(calculNorme(0,0,0,20))
