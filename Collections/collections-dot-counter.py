# collections.Counter()
import collections

num_shoes = int(input())
shoes = collections.Counter(map(int, input().split()))
num_customers = int(input())

income = 0

for i in range(num_customers):
    size, price = map(int, input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1

print(income)
