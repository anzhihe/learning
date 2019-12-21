import os

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n')
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()

print(content)
