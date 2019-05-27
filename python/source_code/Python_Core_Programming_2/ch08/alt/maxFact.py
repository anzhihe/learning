#!/usr/bin/env python
'''
$Id: maxFact.py,v 1.1 2000/03/16 02:33:40 wesc Exp $

maxFact.py -- calculates the largest factor of a number
    (or indicate that it is prime)
'''

#
# calcMaxFac(num) -- return -1 if prime, largest factor otherwise
#
def calcMaxFac(num):
    # composite smallest possible factor is 2
    count = num / 2

    # count backwards to 0 looking for first factor
    while count > 1:

        # break if factor found...
        if (num % count == 0):
            break

        # otherwise decrement and continue
        else:
            count = count - 1

    # reached 1 without finding a factor, ergo prime;
    # (example of while-else statement)
    else:
        return -1

    # return largest factor found
    return count


#
# showMaxFac(x, y) -- return largest factors of numbers from x to y,
#        or an indication a number if prime if applicable
#
def showMaxFacs(x, y):
    for eachNum in range(x, y):
        res = calcMaxFac(eachNum)
        if res == -1:
            print eachNum, 'is prime'
        else:
            print eachNum, 'has a largest factor of', res


# show the largest factors of values 10 - 20 as a test
if __name__ == '__main__':
    showMaxFacs(10, 21)
