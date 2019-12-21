import shelve

# save data to shelf file
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

# read data from shelf file
shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()
