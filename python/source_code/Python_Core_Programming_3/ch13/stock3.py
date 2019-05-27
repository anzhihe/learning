#!/usr/bin/env python

from time import ctime
from urllib.request import urlopen

TICKs = ('yhoo', 'dell', 'cost', 'adbe', 'intc')
URL = 'http://quote.yahoo.com/d/quotes.csv?s=%s&f=sl1c1p2'

print('\nPrices quoted as of: %s\n' % ctime())
print('TICKER', 'PRICE', 'CHANGE', '%AGE')
print('------', '-----', '------', '----')
u = urlopen(URL % ','.join(TICKs))

for row in u:
    tick, price, chg, per = row.decode('utf-8').split(',')
    print(tick, '%.2f' % float(price), chg, per.rstrip())

u.close()
