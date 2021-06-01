# The Captain's Room
K, array = (int(input()), list(map(int, input().split())))
print(((sum(set(array)) * K) - (sum(array))) // (K - 1))
