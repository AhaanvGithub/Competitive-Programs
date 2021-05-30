# Symmetric Difference
len_a, a, len_b, b = (int(input()),input().split(),int(input()),input().split())
print('\n'.join(sorted((set(b).difference(set(a))).union(set(a).difference(set(b))), key=int)))
