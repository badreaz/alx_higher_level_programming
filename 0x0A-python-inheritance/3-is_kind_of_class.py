#!/usr/bin/python3
""" is_kind_of_class definition module """


def is_kind_of_class(obj, a_class):
    """" returns True if the object is an instance
    of, or if the object ian instance of a class
    that inherited from, the specified class; otherwise
    False """
    if isinstance(obj, a_class) or issubclass(obj, a_class):
        return True
    return False
