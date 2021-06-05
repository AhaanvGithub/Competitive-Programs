# Iterables and Iterators
from itertools import combinations

indices = int(input())
lst = list(combinations(input().split(), int(input())))

print(len(list(filter(lambda c: 'a' in c, lst)))/len(lst))
