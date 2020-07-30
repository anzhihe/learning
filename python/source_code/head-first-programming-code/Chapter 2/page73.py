import urllib.request 
import time 

price = 99.99 
while price > 4.74: 
    time.sleep(9)     
    page = urllib.request.urlopen("http://www.beans-r-us.biz/prices.html") 
    text = page.read().decode("utf8") 
    where = text.find('>$') 
    start_of_price = where + 2 
    end_of_price = start_of_price + 4 
    price = float(text[start_of_price:end_of_price]) 
print ("Buy!")
