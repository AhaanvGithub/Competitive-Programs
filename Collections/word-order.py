# Word Order
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict): pass

dict = OrderedCounter(input() for _ in range(int(input())))
print(len(dict))
print(*dict.values())
