#!/usr/bin/env python

dashes = '\n' + '-' * 50
exec_dict = {

'f': """                        # for loop
for %s in %s:
    print %s
""",

's': """                        # sequence while loop
%s = 0
%s = %s
while %s < len(%s):
    print %s[%s]
    %s = %s + 1
""",

'n': """                        # counting while loop
%s = %d
while %s < %d:
    print %s
    %s = %s + %d
"""
}

def main():

    ltype = raw_input('Loop type? (For/While) ')
    dtype = raw_input('Data type? (Number/Sequence) ')

    if dtype == 'n':
        start = input('Starting value? ')
        stop = input('Ending value (non-inclusive)? ')
        step = input('Stepping value? ')
        seq = str(range(start, stop, step))

    else:
        seq = raw_input('Enter sequence: ')

    var = raw_input('Iterative variable name? ')

    if ltype == 'f':
        exec_str = exec_dict['f'] % (var, seq, var)

    elif ltype == 'w':
        if dtype == 's':
            svar = raw_input('Enter sequence name? ')
            exec_str = exec_dict['s'] % \
                (var, svar, seq, var, svar, svar, var, var, var)

        elif dtype == 'n':
            exec_str = exec_dict['n'] % \
                (var, start, var, stop, var, var, var, step)

    print dashes
    print 'The custom-generated code for you is:' + dashes
    print exec_str + dashes
    print 'Test execution of the code:' + dashes
    exec exec_str
    print dashes

if __name__ == '__main__':
    main()
