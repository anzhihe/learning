#!/usr/bin/env python
'''
$Id$

userpw.py -- maintain a "user database" consisting of a set
of login names and corresponding passwords

Exercises:

    7-5a) add a timestamp to the data stored so that the
            user is informed of last successful login

    7-5b) add an "administrative user" which can remove
            users from the database as well as view the
            entire list of current users

    7-5c) add a level of security by encrypting passwords

    7-5d) at a GUI interface if you are familiar with one
            such as Tkinter

    9-13a) store the data base to a disk file so that you
            do not have to "recreate" the database every
            time you run your application

    9-13b) use the pickle module to store the database
            object directly as opposed to writing out the
            data one line at a time
'''
# clear database dictionary
db = {}

#
# newuser() -- create new user and add to database
#
def newuser():
    prompt = 'login desired: '
    while 1:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = raw_input('passwd: ')
    db[name] = pwd


#
# olduser() -- verify password to login existing users
#
def olduser():
    name = raw_input('login: ')
    pwd = raw_input('passwd: ')
    passwd = db.get(name)
    if passwd == pwd:
        pass
    else:
        print 'login incorrect'
        return

    print 'welcome back', name


#
# showmenu() -- interactive portion of application
#        displays menu to prompt user and takes
#        action based on user response
#
def showmenu():
    prompt = """
(N)ew User Login
(E)xisting User Login
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
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice

            # validate option chosen
            if choice not in 'neq':
                print 'invalid menu option, try again'
            else:
                chosen = 1

        # take appropriate action
        if choice == 'q':
            done = 1
        if choice == 'n':
            newuser()
        if choice == 'e':
            olduser()


# run showmenu() as the application
if __name__ == '__main__':
    showmenu()
