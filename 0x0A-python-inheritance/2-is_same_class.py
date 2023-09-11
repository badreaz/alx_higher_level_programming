#!/usr/bin/python3
""" is_same_class definition module """


def is_same_class(obj, a_class):
    """ returns True if the object is exactly an instance of
    the specified class; otherwise False """
    if type(obj) is a_class:
        return True
    return False
