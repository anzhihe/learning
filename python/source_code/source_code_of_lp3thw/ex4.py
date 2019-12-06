cars = 100
space_in_a_car = 4.0 #多了个小数点
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car #引入了1个小数点。
average_passengers_per_car = passengers / cars_driven #整数处以整数，为何得出有小数点的。


print ("There are", cars,"cars availabe.")
print ("There are only",drivers,"drivers availabe.")
print ("There will be" , cars_not_driven,"empty cars today.")
print ("We can transport",carpool_capacity,"people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car,"in each car.")

'''
运行后的结果：
itifadeMacBook-Pro:LP3THW yyy$ python ex4.py
There are 100 cars availabe.
There are only 30 drivers availabe.
There will be 70 empty cars today.
We can transport 120.0 people today.
We have 90 to carpool today.
We need to put about 3.0 in each car.
'''
