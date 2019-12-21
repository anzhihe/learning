def commaList(items):
    ret = ''
    for item in items[:-1]:
        ret += item + ', '
    return ret + 'and ' + items[-1]

spam = ['apples', 'bananas', 'tofu', 'cats']
print(commaList(spam))
