# Set Mutations
not_using, a = int(input()), set(map(int, input().split()))

n = int(input())

for i in range(n):
    comm, ne = input().split()
    B = set(map(int, input().split()))

    if comm == 'intersection_update':
        a.intersection_update(B)
    elif comm == 'update':
        a.update(B)
    elif comm == 'difference_update':
        a.difference_update(B)
    elif comm == 'symmetric_difference_update':
        a.symmetric_difference_update(B)

print(sum(a))
