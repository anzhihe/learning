def spam():
    global eggs # this is the global
    eggs = 'spam'

def bacon():
    eggs = 'bacon' # this is a local

def ham():
    print(eggs) # this is the global

eggs = 42 # this is the global
spam()
print(eggs)
