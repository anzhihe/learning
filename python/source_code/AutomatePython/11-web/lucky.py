#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Baiduing...') # display text while downloading the Google page
res = requests.get('http://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
linkElems = soup.select('h3 a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    #print(linkElems[i].get('href'))
    webbrowser.open(linkElems[i].get('href'))
