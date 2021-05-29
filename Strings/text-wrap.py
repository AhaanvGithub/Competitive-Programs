# Text Wrap
import textwrap


def wrap(string, max_width):
    split_string = []
    for i in range(0, len(string), max_width):
        split_string.append(string[i:i + max_width])

    return '\n'.join([i for i in split_string[:]])


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
