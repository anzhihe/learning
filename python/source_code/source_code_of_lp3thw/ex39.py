# 创造一个州的缩写制图-字典？
states = {#这里建立了一个‘字典’的数据类型，也就是说一个变量，它用大括号括着，里面是dic= {A：B，C：D，E:F}的格式，通过索引 A C E 分别可以调用出 B D F 这三个。
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# 创建一个州的基本设置，以及它们中的一些城市
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# 增加一些城市
cities['NY']= 'New York'#调用字典数据类型的一种方法：对该字典，以切片的方法,给原来的字典增加新的内容，具体的就是 dic[‘G’]=‘H’；这样原来字典中就多了一组数据：G:H
cities['OR']= 'Porland'

# 打印出一些城市
print('-' * 10)
print("NY States has: ", cities['NY'])#这里说明一种调用字典内容的方法，通过dic['G']可以调用出其代表的‘H’
print("OR State has: ", cities['OR'])

# 打印一些州
print('-' * 10)
print("Michigan's abbreviation is:", states['Michigan'])#这里同样是通过索引 G 调用 H 的方法。当然这里 print 方法里也是print（"字符串"，变量）的方法。
print("Florida's abbreviation is :", states['Florida'])

# do it by using the state then cities dict使用州的字典和城市的字典
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])#这里首先用“州-字典”所用调用了这个‘州名-缩写’；又利用“城市字典”调用了‘州名-缩写’这个变量，调用了‘所在州的大城市名’
print("Florida has:", cities[states['Florida']])

# print every state abbreviation打印每个州的缩写
print('-' * 10)

print("---注，这里的数据是 元组数组：", states.items()) #------ 这一行是新加的，是为了看明白所谓的元组是啥样的。他不能被修改？
print("----注，这里的数据是 列表： ", list(states.items()) ) #------ 这一行是新加的，是为了看明白所谓的元组是啥样的。他不能被修改？

for state, abbrev in list(states.items()):# 建立了一个 for 循环，循环变量是 州名state、州名缩写abbrev，分别将states字典里各组循环了一遍.
    print(f"{state} is abbreviated {abbrev}")#注意：list(states.items())的意思：先对states这个变量使用items()方法（函数）-Python 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组。
#list() 方法用于将元组转换为列表。注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。
# print every city in states打印州里的每个城市

print('_' * 10)

for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time 同时使用两个字典。
print('-' * 10)

for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10 )
# safely get a abbreviation by state that might not be there
state = states.get('Texas')#Python 字典 get() 函数返回指定键的值，如果值不在字典中返回默认值.dict.get(key, default=None)

if not state:# 逻辑判断：not False= Ture
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')#get()方法：通过关键词 TX 来寻找字典，如果没有，则返回Does Not Exist
print(f"The city for the state 'TX' is: {city} ")#变量city所承载的信息转入到了这里。


# 既能像字典一样，有具有“顺序”，那么请你上网查查——collections.OrderedDict数据结构。

'''
# 运行后的结果 1：
bogon:lp3thw yyy$ python ex39.py
----------
NY States has:  New York
OR State has:  Porland
----------
Michigan's abbreviation is: MI
Florida's abbreviation is : FL
----------
Michigan has:  Detroit
Florida has: Jacksonville
----------
Oregon is abbreviated OR
Florida is abbreviated FL
California is abbreviated CA
New York is abbreviated NY
Michigan is abbreviated MI
__________
CA has the city San Francisco
MI has the city Detroit
FL has the city Jacksonville
NY has the city New York
OR has the city Porland
----------
Oregon state is abbreviated OR
and has city Porland
Florida state is abbreviated FL
and has city Jacksonville
California state is abbreviated CA
and has city San Francisco
New York state is abbreviated NY
and has city New York
Michigan state is abbreviated MI
and has city Detroit
----------
Sorry, no Texas.
The city for the state 'TX' is: Does Not Exist




# 运行后的结果 2：

bogon:lp3thw yyy$ python ex39.py
----------
NY States has:  New York
OR State has:  Porland
----------
Michigan's abbreviation is: MI
Florida's abbreviation is : FL
----------
Michigan has:  Detroit
Florida has: Jacksonville
----------
---注，这里的数据是 元组数组： dict_items([('Oregon', 'OR'), ('Florida', 'FL'), ('California', 'CA'), ('New York', 'NY'), ('Michigan', 'MI')])
----注，这里的数据是 列表：  [('Oregon', 'OR'), ('Florida', 'FL'), ('California', 'CA'), ('New York', 'NY'), ('Michigan', 'MI')]
Oregon is abbreviated OR
Florida is abbreviated FL
California is abbreviated CA
New York is abbreviated NY
Michigan is abbreviated MI
__________
CA has the city San Francisco
MI has the city Detroit
FL has the city Jacksonville
NY has the city New York
OR has the city Porland
----------
Oregon state is abbreviated OR
and has city Porland
Florida state is abbreviated FL
and has city Jacksonville
California state is abbreviated CA
and has city San Francisco
New York state is abbreviated NY
and has city New York
Michigan state is abbreviated MI
and has city Detroit
----------
Sorry, no Texas.
The city for the state 'TX' is: Does Not Exist

'''
