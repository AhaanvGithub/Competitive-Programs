# Swap Case
def swap_case(s):
    return s.swapcase()
    
    """
    That is pretty much cheating, so here is the logic:
        return "".join([i.lower() if i.isupper() else i.upper() for i in s])
    """

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

    
# String Split and Join
def split_and_join(line): 
    return '-'.join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
    
# What's your name?
def print_full_name(first, last):
    print(f'Hello {first} {last}! You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
    
    
# Mutations
def mutate_string(string, position, character):
    string = string[:position] + character + string[position + 1:]
    return string
        

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
    
# Find a string
def count_substring(string, sub_string):
    count = 0
    
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
            
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
    
# String Validators
if __name__ == '__main__':
    s = input()
    
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
    
    
# Text Alignment
thickness = int(input())
c = 'H'

for i in range(thickness): print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
for i in range(thickness+1): print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
for i in range((thickness+1)//2): print((c*thickness*5).center(thickness*6))    
for i in range(thickness+1): print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
for i in range(thickness): print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

  
# Text Wrap
import textwrap

def wrap(string, max_width):
    split_string = []
    for i in range(0, len(string), max_width):
        split_string.append(string[i:i + max_width])
        
    return '\n'.join([i for i in split_string[:]])
    
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
    
# Designer Door Mat
N, M = map(int,input().split())

for i in range(1, N, 2): 
    print((i * ".|.").center(M, "-"))
    
print("WELCOME".center(M, "-"))

for i in range(N - 2 ,- 1, - 2): 
    print((i * ".|.").center(M, "-"))


# String Formatting
def print_formatted(n):
    results = []

    for i in range(1, n+1):
        decimal = str(i)
        octal = str(oct(i)[2:])
        hex_ = str(hex(i)[2:]).upper()
        binary = str(bin(i)[2:])

        results.append([decimal, octal, hex_, binary])

    width = len(results[-1][3])

    for i in results:
        print(*(rep.rjust(width) for rep in i))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# Alphabet Rangoli
 def print_rangoli(n):
    import string
    alpha = string.ascii_lowercase

    l = []
    
    for i in range(n):
        s = "-".join(alpha[i:n])
        l.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
        
    print('\n'.join(l[:0:-1] + l))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# Capitalize!
#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    return ' '.join(map(str.capitalize, s.split(' ')))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# The Minion Game
def minion_game(s):

    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s) - i)
        else:
            stusc += (len(s) - i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)


# Merge the Tools!
def merge_the_tools(string, k):
    num_subsegments = int(len(string) / k)

    for i in range(num_subsegments):
        t = string[i * k : (i + 1) * k]
    
        u = ""
    
        for c in t:
            if c not in u: u = u + c
                
        print(u)
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
