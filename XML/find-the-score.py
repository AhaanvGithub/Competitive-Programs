# XML 1 - Find the Score
import xml.etree.ElementTree as Tree


def get_attr_number(node):
    return sum(len(elem.items()) for elem in Tree.iter())
