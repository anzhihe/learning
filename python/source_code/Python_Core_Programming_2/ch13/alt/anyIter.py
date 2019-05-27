#!/usr/bin/env python

class AnyIter:  # any number of items iterator
    def __init__(self, data, safe=0):
        self.safe = safe        # play it safe
        self.iter = iter(data)  # our iterator

    def __iter__(self):         # class iterator
        return self

    def next(self, howmany=1):  # special next()
        retval = []
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.next())
            except StopIteration:
                # reraise if asking for too
                # many items
                if self.safe == 0:
                    raise
                # "safe" mode: return less than
                # requested
                else:
                    break
        return retval
