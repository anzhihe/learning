#!/usr/bin/env python

class HotelRoomCalc:
    'Hotel room rate calculator'
   
    # constructor, set default sales and room tax rates
    def __init__(self, rt, sales=0.085, rm=0.1):
        'HotelRoolCalc default args: sales tax == 8.5% & room tax == 10%'
        self.salesTax = sales	# set sales tax rate
        self.roomTax = rm	# set room tax rate
        self.roomRate = rt	# set daily room rate

    # calculate total due, defaulting to a 1-day stay
    def calcTotal(self, days=1):
        'Calculate total; default to daily rate'

	# calculate total... take room rate, add sales
	# and room taxes and round to 2 decimal places
        daily = round((self.roomRate * (1 + self.roomTax + self.salesTax)), 2)

	# now multiply by length of stay and return
        return float(days) * daily
