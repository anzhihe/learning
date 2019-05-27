#!/usr/bin/env python

from warnings import warn

class ReqStrSugRepr(object):

    def __init__(cls, name, bases, attrd):
        super(ReqStrSugRepr, cls).__init__(
            name, bases, attrd)

        if '__str__' not in attrd:
            raise TypeError(
                "Class requires overriding of __str__()")

        if '__repr__' not in attrd:
            warn(
            'Class suggests overriding of __repr__()\n',
                stacklevel=3)

print '*** Defined ReqStrSugRepr (meta)class\n'

class Foo(object):
    __metaclass__ = ReqStrSugRepr

    def __str__(self):
        return 'Instance of class:', \
            self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__

print '*** Defined Foo class\n'

class Bar(object):
    __metaclass__ = ReqStrSugRepr

    def __str__(self):
        return 'Instance of class:', \
            self.__class__.__name__

print '*** Defined Bar class\n'

class FooBar(object):
    __metaclass__ = ReqStrSugRepr

print '*** Defined FooBar class\n'
