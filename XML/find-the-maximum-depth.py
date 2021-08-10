# XML2 - Find the Maximum Depth
max_depth = 0


def depth(elem, level):
    global max_depth
    if level == max_depth:
        max_depth += 1

    for child in elem:
        depth(child, level + 1)
