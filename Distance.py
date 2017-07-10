c1=[4,3]
c2=[6,4]
c3=[9,3]
c4=[4,6]
c4=[5,4]
c6=[11,6]
import math

def calculateDistance(x1,y1,x2,y2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return dist

A1 = calculateDistance(4,3,6,4)
A2 = calculateDistance(9,3,4,6)
A3 = calculateDistance(5,4,11,6)
C4 = [A1,A2,A3]
print ("Min:",     min(C4))
print ("Max:",     max(C4))

