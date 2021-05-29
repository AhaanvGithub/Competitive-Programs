# Swap Case
def swap_case(s):
    return s.swapcase()

    """
    That is pretty much cheating, so here is the logic:
        return "".join([i.lower() if i.isupper() else i.upper() for i in s])
    """


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
