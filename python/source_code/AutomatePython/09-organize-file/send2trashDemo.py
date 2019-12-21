import send2trash

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

send2trash.send2trash('bacon.txt')