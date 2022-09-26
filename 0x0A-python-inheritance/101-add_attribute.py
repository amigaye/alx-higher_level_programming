#!/usr/bin/python3
"""add attribute
"""


def add_attribute(*args):
    """ Function that adds a new attribute to an object

    Args:
        obj: object
        name: attribute name
        value: attribute value

    Raises:
        TypeError: when the attribute can't be added

    """

    if "main" in str(type(args[0])):
        setattr(args[0], args[1], args[2])
    else:
        raise TypeError("can't add new attribute")
