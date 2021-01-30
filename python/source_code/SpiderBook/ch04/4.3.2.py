#coding:utf-8
import bs4
from bs4 import BeautifulSoup
html_str = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2"><!-- Lacie --></a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html_str,'lxml', from_encoding='utf-8')
print soup.prettify()

print soup.name
print soup.title.name

soup.title.name = 'mytitle'
print soup.title
print soup.mytitle
soup.mytitle.name = 'title'
print soup.p['class']
print soup.p.get('class')


print soup.p.attrs
soup.p['class']="myClass"
print soup.p

print soup.p.string
print type(soup.p.string)

print type(soup.name)
print soup.name
print soup.attrs


print soup.a.string
print type(soup.a.string)

if type(soup.a.string)==bs4.element.Comment:
    print soup.a.string

print soup.head.contents
print len(soup.head.contents)
print soup.head.contents[0].string
for child in soup.head.children:
    print(child)
for child in soup.head.descendants:
    print(child)


print soup.head.string
print soup.title.string
print soup.html.string

for string in soup.strings:
    print(repr(string))

for string in soup.stripped_strings:
    print(repr(string))

print soup.title
print soup.title.parent

print soup.a
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

print soup.p.next_sibling
print soup.p.prev_sibling
print soup.p.next_sibling.next_sibling

for sibling in soup.a.next_siblings:
    print(repr(sibling))

print soup.head
print soup.head.next_element

for element in soup.a.next_elements:
    print(repr(element))

print soup.find_all('b')

import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

print soup.find_all(["a", "b"])

for tag in soup.find_all(True):
    print(tag.name)
def hasClass_Id(tag):
    return tag.has_attr('class') and tag.has_attr('id')
print soup.find_all(hasClass_Id)

print soup.find_all(id='link2')

print soup.find_all(href=re.compile("elsie"))

print soup.find_all(id=True)
print soup.find_all("a", class_="sister")

print soup.find_all(href=re.compile("elsie"), id='link1')

data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
data_soup.find_all(attrs={"data-foo": "value"})


print soup.find_all(text="Elsie")
print soup.find_all(text=["Tillie", "Elsie", "Lacie"])
print soup.find_all(text=re.compile("Dormouse"))

print soup.find_all("a", text="Elsie")

print soup.find_all("a", limit=2)

print soup.find_all("title")
print soup.find_all("title", recursive=False)


#直接查找title标签
print soup.select("title")
#逐层查找title标签
print soup.select("html head title")
#查找直接子节点
#查找head下的title标签
print soup.select("head > title")
#查找p下的id="link1"的标签
print soup.select("p > #link1")
#查找兄弟节点
#查找id="link1"之后class=sisiter的所有兄弟标签
print soup.select("#link1 ~ .sister")
#查找紧跟着id="link1"之后class=sisiter的子标签
print soup.select("#link1 + .sister")

print soup.select(".sister")
print soup.select("[class~=sister]")

print soup.select("#link1")
print soup.select("a#link2")

print soup.select('a[href]')

print soup.select('a[href="http://example.com/elsie"]')
print soup.select('a[href^="http://example.com/"]')
print soup.select('a[href$="tillie"]')
print soup.select('a[href*=".com/el"]')

