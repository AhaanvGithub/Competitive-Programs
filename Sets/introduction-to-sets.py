# Introduction to Sets
def average(array):
    new_set = set(array)
    return sum(new_set)/len(new_set)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
