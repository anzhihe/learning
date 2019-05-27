#!/usr/bin/env python
'''
$Id$

stack.py -- simulate stack data structures using lists

Exercises:

    13-8) create a Stack class

    13-10) create a class similar to arrays in Perl which have
            both queue- and stack-like qualities and features
'''

# create our data structure
stack = []

#
# pushit() -- adds stirng to the stack
#
def pushit():
    stack.append(raw_input('Enter new string: '))

#
# popit() -- removes stirng from the stack
#
def popit():
    if len(stack) == 0:
        print 'Cannot pop from an empty stack!'
    else:
        print 'Removed [', stack.pop(), ']'

#
# viewstack() -- display stack contents
#
def viewstack():
    print str(stack)

#
# showmenu() -- interactive portion of application
#        displays menu to prompt user and takes
#        action based on user response
#
def showmenu():

    # using triple quotes to help us put together
    # the multi-line string prompt to display
    prompt = """
p(U)sh
p(O)p
(V)iew
(Q)uit

Enter choice: """

    # loop until user quits
    done = 0
    while not done:

        # loop until user choses valid option
        chosen = 0
        while not chosen:

            # if user hits RETURN/Enter, ^C, or ^D (EOF),
            # pretend they typed 'q' to quit normally
            try:
                choice = raw_input(prompt)[0]
            except (IndexError, EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice

            # validate option chosen
            if choice not in 'uovq':
                print 'invalid option, try again'
            else:
                chosen = 1

        # take appropriate action
        if choice == 'q':
            done = 1
        if choice == 'u':
            pushit()
        if choice == 'o':
            popit()
        if choice == 'v':
            viewstack()

# run showmenu() as the application
if __name__ == '__main__':
    showmenu()
