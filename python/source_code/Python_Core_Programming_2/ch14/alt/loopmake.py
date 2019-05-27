#!/usr/bin/env python
# $Id: loopmaker.py,v 1.7 2000/04/22 01:44:26 wesc Exp $
#
# loopmaker.py -- CASE script: creates Python loops given parameters
#
# created on 00/04/21 by wesc
#

from keyword import iskeyword

# setup exec_str dictionary
exec_dict = {

# FOR loop
'f': '''
for %s in %s:
    print %s
''',

# WHILE loop (sequences)
's': '''
%s = 0
%s = %s
while %s < len(%s):
    print %s[%s]
    %s = %s + 1
''',

# WHILE loop (numbers)
'n': '''
%s = %d
while %s < %d:
    print %s
    %s = %s + %d
'''
}

dashes = '\n' + ('-' * 50)
def dashedprint(data, dashes=dashes):
    print data + dashes

def main():

    # prompt for loop type
    while 1:
        ltype = raw_input('Loop type? ([F]or/While) ')
        if not ltype: ltype = 'f'
        if ltype[0] in 'fw':
            break

    # prompt for data type
    while 1:
        dtype = raw_input('Data type? ([N]umber/Sequence [str,list,tuple]) ')
        if not dtype: dtype = 'n'
        if dtype[0] in 'ns':
            break

    # NUMBER type
    if dtype == 'n':
        while 1:
            start = raw_input('Starting value? [0] ')
            if not start:
                start = 0
            else:
                start = int(start)
            while 1:
                stop = input('Ending value (non-inclusive)? ')
                if type(stop) != type(0):
                    print '*** Ending value must be an integer\n'
                else:
                    break
            step = raw_input('Stepping value? [1] ')
            if not step:
                step = 1
            else:
                step = int(step)
            seq = str(range(start, stop, step))
            if seq == '[]':
                ans = raw_input('*** Invalid range; change your values? ([y]/n) ')
                if not ans or ans[0] == 'y':
                    continue
                print
            break

    # SEQUENCE type
    else:
        while 1:
            seq = raw_input('Enter sequence (string, list, or tuple): ')

            try:
                test = eval(seq)

            # invalid sequence... reprompt
            except SyntaxError:
                # keyword can be a string
                if iskeyword(seq):
                    test = seq = `seq`
                else:
                    print "*** Invalid Python sequence data '%s'\n" % seq
                    continue

            # user typed in string without the quotes... add the quotes using repr()
            except NameError:
                test = seq = `seq`

            # must be string, list, or tuple
            if type(test) != type('') and type(test) != type([]) and type(test) != type(()):
                print "*** Invalid Python sequence data '%s'\n" % seq
                continue

            break

    # iterator variable
    while 1:
        var = raw_input('Enter iterative variable name? ')
        if not var:
            print '*** Identifier name is required!\n'
        elif iskeyword(var) or var in dir(__builtins__):
            print "*** Identifier '%s' name is a keyword or built-in!\n" % var
        else:
            try:
                exec var + '=0'
            except SyntaxError:
                print "*** Invalid identifier '%s'!\n" % var
                continue
            break

    # FOR loop
    if ltype == 'f':
        exec_str = exec_dict['f'] % (var, seq, var)

    # WHILE loop
    elif ltype == 'w':

        # sequence length variable (only for sequences)
        if dtype == 's':
            while 1:
                svar = raw_input('Enter sequence name? ')
                if not svar:
                    print '*** Identifier name is required for while loops!\n'
                elif iskeyword(svar) or svar in dir(__builtins__):
                    print "*** Identifier '%s' name is a keyword or built-in!\n" % svar
                else:
                    break
        else:
            svar = None

        # must assign to sequence var if using sequences
        if dtype == 's':
            exec_str = exec_dict['s'] % (var, svar, seq, var, svar, svar, var, var, var)

        # use range() values for loop if using numbers
        elif dtype == 'n':
            exec_str = exec_dict['n'] % (var, start, var, stop, var, var, var, step)

    # EXECUTE code
    dashedprint('')
    dashedprint('The custom-generated code for you is:')
    dashedprint(exec_str)
    dashedprint('Test execution of the code:')
    exec exec_str
    dashedprint('')


# top-level executes main()
if __name__ == '__main__':
    print 'Welcome to Loop Maker v1.0\n'

    while 1:
        main()
        try:
            again = raw_input('Try again? ([Y]es/No) ')
        except:
            print
            break
        if again and again[0] != 'y':
            break
