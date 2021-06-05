# Maximize It!
from itertools import product

k, m = map(int, input().split())
n = []

for i in range(k):
    n.append(list(map(int, input().split()))[1:])

print(max(map(lambda x: sum(i ** 2 for i in x) % m, product(*n))))
