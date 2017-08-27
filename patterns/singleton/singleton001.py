#!/usr/bin/env python

"""Singleton Design Pattern Example."""

class Singleton(object):
    """Defining our example singleton pattern."""

    def __init__(self):
        """Empty __init__ method for now."""
        pass

    def isString(self, input_value):
        """Verify that the input type is a string."""

        if type(input_value) == str:
            return input_value

        return str(input_value)


class NewClass(Singleton, object):

    def __init__(self, name):
        self.name = self.isString(name) if name else "Anonymous"

        print "NewClass defined with name %s" % (self.name)

    def __str__(self):
        return "NewClass %s" % (self.name)

    def __repr__(self):
        return "<NewClass %s>" % (self.name)

    def __hash__(self):
        return hash((self.name, "loves to", "farm"))

_example = NewClass('Joshua')
_example = NewClass(12)
_example = NewClass(None)

print _example.__str__()
print _example.__repr__()
