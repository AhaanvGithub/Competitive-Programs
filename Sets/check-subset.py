# Check Subset
for i in range(int(input())):
    a_len, a, = int(input()), set(input().split())
    b_len, b = int(input()), set(input().split())
    print(a.issubset(b))
