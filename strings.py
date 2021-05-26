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

