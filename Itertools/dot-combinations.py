# itertools.combinations()
from itertools import combinations
ls = input().split()
for size in range(int(ls[1])):
    print(*map("".join, combinations(sorted(ls[0]), size + 1)),sep="\n")
