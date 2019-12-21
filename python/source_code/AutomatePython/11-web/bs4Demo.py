import requests
import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')

elems = exampleSoup.select('#author')
print(elems[0].getText())
print(elems[0].get('id'))
print(elems[0].attrs)
