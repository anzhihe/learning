>>> reversed('abc')
<reversed object at 0x00B42BD0>
>>> sorted('abc')
['a', 'b', 'c']
>>> sorted('wesley foo bar')
[' ', ' ', 'a', 'b', 'e', 'e', 'f', 'l', 'o', 'o', 'r', 's', 'w', 'y']
>>> for i in reversed('wesley foo bar'):
	print i,

	
r a b   o o f   y e l s e w
>>> for i in reversed(['wesley', 'foo', 'bar']):
	print i,

	
bar foo wesley
>>> sorted(['wesley', 'foo', 'bar'])
['bar', 'foo', 'wesley']
>>> 

>>> s = 'thequickbrownfoxjumpedoverthelazydog'
>>> reversed(s)
<reversed object at 0x38bef0>
>>> for t in reversed(s):
...  print t,
...
g o d y z a l e h t r e v o d e p m u j x o f n w o r b k c i u q e h t
>>> sorted(s)
['a', 'b', 'c', 'd', 'd', 'e', 'e', 'e', 'e', 'f', 'g', 'h', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'o', 'o', 'o', 'p', 'q', 'r', 'r', 't', 't', 'u', 'u', 'v', 'w', 'x', 'y', 'z']
>>>
>>> s = 'foobar'
>>> for t in reversed(s):
...  print t,
...
r a b o o f
>>> sorted(s)
['a', 'b', 'f', 'o', 'o', 'r']
>>> s = ['They', 'stamp', 'them', 'when', "they're", 'small']
>>> for t in reversed(s):
...  print t,
...
small they're when them stamp They
>>> sorted(s)
['They', 'small', 'stamp', 'them', "they're", 'when']

