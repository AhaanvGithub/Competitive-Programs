# Python If-Else
#!/bin/python3
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    if (n % 2 == 1) or (n % 2 == 0 and 6 <= n <= 20): print("Weird")
    elif (2 <= n <= 5) or (n > 20): print("Not Weird")
