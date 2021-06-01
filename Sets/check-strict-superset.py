# Check Strict Superset
A, n = set(input().split()), int(input())
print(all([A.issuperset(set(input().split())) for _ in range(n)]))
