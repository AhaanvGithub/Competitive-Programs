# Merge the Tools!
def merge_the_tools(string, k):
    num_subsegments = int(len(string) / k)

    for i in range(num_subsegments):
        t = string[i * k: (i + 1) * k]

        u = ""

        for c in t:
            if c not in u: u = u + c

        print(u)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
