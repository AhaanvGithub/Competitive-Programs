# Lists
if __name__ == '__main__':
    n = int(input())
    ls = []

    for _ in range(n):

        s = input().split()

        if s[0] != "print":
            s[0] = s[0] + "(" + ",".join(s[1:]) + ")"
            eval("ls." + s[0])
        else:
            print(ls)
