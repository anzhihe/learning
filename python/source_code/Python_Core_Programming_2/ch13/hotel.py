class HotelRoomCalc:
    'Hotel room rate calculator'
   
    def __init__(self, rt, sales=0.085, rm=0.1):
        '''HotelRoolCalc default arguments:
        sales tax == 8.5% and room tax == 10%'''
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self, days=1):
        'Calculate total; default to daily rate'
        daily = round((self.roomRate * \
            (1 + self.roomTax + self.salesTax)), 2)
        return float(days) * daily
