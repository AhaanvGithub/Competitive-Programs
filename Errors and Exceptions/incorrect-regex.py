# Incorrect Regex
import re

for i in range(int(input())):
    try:
        re.compile(input())
        is_valid = True
    except re.error:
        is_valid = False

    print(is_valid)
