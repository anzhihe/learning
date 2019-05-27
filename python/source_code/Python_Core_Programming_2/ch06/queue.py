#!/usr/bin/env python

queue = []

def enQ():
    queue.append(raw_input('Enter new queue element: '))

def deQ():
    if len(queue) == 0:
        print 'Cannot dequeue from empty queue!'
    else:
        print 'Removed [', queue.pop(0), ']'

def viewQ():
    print str(queue)

def showmenu():
    prompt = """
(E)nqueue
(D)equeue
(V)iew
(Q)uit

Enter choice: """

    done = 0
    while not done:

        chosen = 0
        while not chosen:
            try:
                choice = raw_input(prompt)[0]
            except (IndexError, EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'devq':
                print 'invalid option, try again'
            else:
                chosen = 1

        if choice == 'q': done = 1
        if choice == 'e': enQ()
        if choice == 'd': deQ()
        if choice == 'v': viewQ()

if __name__ == '__main__':
    showmenu()
