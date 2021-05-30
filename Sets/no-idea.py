# No Idea!
N, M = input().split(" ")
arr = input().split(" ")
A = set(input().split(" "))
B = set(input().split(" "))
happiness = 0

for i in arr:
    if i in A and i not in B: happiness += 1
    if i in B and i not in A: happiness -= 1

print(happiness)
