# ginortS
lower, upper, odd, even = [], [], [], []
for i in sorted(input()):
    if i.isalpha():
        x = upper if i.isupper() else lower
    else:
        x = odd if int(i) % 2 else even
    x.append(i)
print("".join(lower + upper + odd + even))
