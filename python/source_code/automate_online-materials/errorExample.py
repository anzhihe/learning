def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

spam()
