# Hello World
print("Hello, World!")


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
      
      
# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a // b, "\n", a / b)

    
# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(
        f'{a + b} \n'
        f'{a - b} \n'
        f'{a * b}'
    )

    
# Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(0, n, 1): print(i**2)

      
# Write a function
def is_leap(year):
    leap = False
    
    # Write your logic here
    leap = year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    return leap

year = int(input())


# Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1): print(i, end="")
