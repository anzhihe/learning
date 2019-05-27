#!/usr/bin/env python
# $Id: moneyfmt.py,v 1.2 2000/02/07 07:46:09 wesc Exp $
#
# moneyfmt.py -- create a class that prints a floating-point
#        value in a financial format
#
# created 00/02/07 by wesc
#

"""Implements the Dollar class for displaying a financial
    format for single floating-point values.  Also see
    moneyfmt.MoneyFmt.__doc__.
"""

class MoneyFmt(object):

    """This class...

        x = dollar.Dollar(amount)        # amount is a float

        NOTE:  str() will give the formatted display while repr() and `` will
            give the raw float value.  This allows for both pretty-printing
            output as well as the ability to still manipulate the values.

        Methods:

            x.update([amount]) -- updates the value of the number
    """

    def __init__(self, value=0.):                # constructor

        self.value = float(value)


    def update(self, value=None):                # allow updates

        """x.update([amount])
                You can update the amount with this method.
                If the value is missing, the value is not updated.
                Also see moneyfmt.MoneyFmt.__doc__.
        """

        ###
        ###        (a) FILL THIS IN
        ###


    def __nonzero__(self):                        # boolean test (same as float)

            return int(self.value)


    def __repr__(self):                                # standalone, as a float number

        return str(self.value)


    def __str__(self):                                # display in requested format

        val = ''

        ###
        ###        (b) FILL THIS IN... don't forget about negative numbers too!!
        ###

        return val
