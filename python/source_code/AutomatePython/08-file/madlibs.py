import re

text = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."

regex = '[A-Z]{2,}'
wordsRegex = re.compile(regex)

while True:
    mo = wordsRegex.search(text)
    if mo == None:
        #print('No words to be replaced.')
        break
    word = input('Enter an ' + mo.group().lower() + ':\n')
    text = wordsRegex.sub(' '+word, text, count=1)

print(text)
   