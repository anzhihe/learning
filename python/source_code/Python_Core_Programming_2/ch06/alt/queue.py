#!/usr/bin/env python
'''
$Id$

queue.py -- simulate queue data structures using lists

NOTE:  as of the time of publication, there is a bug in JPython1.1
    that does not recognize arguments for the list pop() method:
    TypeError: pop(): expected 0 args; got 1

Exercises:

    13-9) create a Queue class

    13-10) create a class similar to arrays in Perl which have
            both queue- and stack-like qualities and features
'''

# create our data structure
queue = []

#
# enQ() -- add string to end of queue
#
def enQ():
    queue.append(raw_input('Enter new queue element: '))

#
# deQ() -- remove string from front of queue
#
def deQ():
    if len(queue) == 0:
        print 'Cannot dequeue from empty queue!'
    else:
        print 'Removed [', queue.pop(0), ']'

#
# viewQ() -- display queue contents
#
def viewQ():
    print str(queue)

#
# showmenu() -- interactive portion of application
#        displays menu to prompt user and takes
#        action based on user response
#
def showmenu():
    prompt = """
(E)nqueue
(D)equeue
(V)iew
(Q)uit

Enter choice: """

    # loop until user quits
    done = 0
    while not done:

        # loop until user choses valid option
        chosen = 0
        while not chosen:

            # if user hits ^C or ^D (EOF),
            # pretend they typed 'q' to quit
            try:
                choice = raw_input(prompt)[0]
            except (IndexError, EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice

            # validate option chosen
            if choice not in 'devq':
                print 'invalid option, try again'
            else:
                chosen = 1

        # take appropriate action
        if choice == 'q':
            done = 1
        if choice == 'e':
            enQ()
        if choice == 'd':
            deQ()
        if choice == 'v':
            viewQ()

# run showmenu() as the application
if __name__ == '__main__':
    showmenu()
