# Compress the String!
from itertools import groupby

for k, c in groupby(input()):
        a = list(c)
        print("(", len(a), ", ", a[0], ")", end = " ", sep = "")
