#!/usr/bin/env python

class MoneyFmt(object):
    def __init__(self, value=0.0):		# constructor
        self.value = float(value)

    def update(self, value=None):		# allow updates
        ###
        ### (a) complete this function
        ###

    def __repr__(self):				# display as a float
        return `self.value`

    def __str__(self):				# formatted display
        val = ''

        ###
        ### (b) complete this function... do NOT
        ###     forget about negative numbers too!!
        ###

        return val

    def __nonzero__(self):			# boolean test
        ###
        ### (c) find and fix the bug
        ###

	return int(self.value)
