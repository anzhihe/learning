#!/usr/bin/env python
'''
$Id$

cardrun.py -- "credit card run" script serves as a demo for a
    ficticious credit card transaction processing application
    which reads data in from a file and uses the safe_float()
    function along with try-except to safely "ignore bad data" 
    such as string text as opposed to strictly numerical input.
'''

# safe_float() --> float
def safe_float(object):
    'safe_float() converts strings to floats "safely"'

    # attempt to convert object using float()
    try:
        retval = float(object)

    # failure return value is error reason
    except (TypeError, ValueError), e:
        retval = str(e)

    return retval


# main() --> None
def main():
    'main() handles all the data processing'

    # attempt to open data file
    try:
        ccfile = open('carddata.txt', 'r')

    # display error reason on failure
    except IOError, e:
        print 'file open failed:', e
        return

    # otherwise show a diagnostic 'ok'
    else:
        print 'file opened successfully'

    # read all data and close file
    txns = ccfile.readlines()
    ccfile.close()

    # processing setup
    total = 0.00
    print 'processing new account, log:'

    # look at each transaction
    for eachTxn in txns:
        result = safe_float(eachTxn)

        # string indicates failure ...
        if isinstance(result, basestring):
            if eachTxn[0] == '#':
                print 'comment... ignored'
            else:
                print '\ncategory:', eachTxn

        # ... while float means success
        elif isinstance(result, float):
            total += result
            print 'processing transaction of: %.2f' % result

        # unknown return type from safe_float()
        else:
            print 'invalid return type from safe_float()... ignored'

    # display final totals
    print 'new balance: $%.2f' % (total)

# call main() if invoked as script
if __name__ == '__main__':
    main()
