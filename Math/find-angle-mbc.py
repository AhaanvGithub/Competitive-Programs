# Find Angle MBC
from math import *

abdist = float(input())
bcdist = float(input())
print(str(int(round(degrees(atan(abdist/bcdist)),0))) + "\N{DEGREE SIGN}")