#  设置：给变量 车（cars）赋值100，每量车的空是4.0，司机是30个，旅客是90个。
# 车数量为100
cars = 100
# 每辆车里等空位是4
space_in_a_car = 4.0 #思考：这里为什么要用4.0浮点计算而不是4？
# 司机数量是30个。
drivers = 30
# 旅客人数为90个。
passengers =90

# 参数设置&参数计算：没有人开的车=车总数-司机数；有人开的车数=司机数量；有效空间数量=有人开的车数*每量车上的空。每辆车桑拿的平均旅客数=旅客总数／有人开的车数。

cars_not_driven = cars -drivers

cars_driven = drivers

carpool_capacity= cars_driven * space_in_a_car

average_passengers_per_car= passengers / cars_driven

# 打印 （字符串，变量-车总数，字符串）

print("There are", cars, "cars available.")

print ("There are only",drivers, "drivers available.")

print ("There will be", cars_not_driven,"empty cars today.")

print ("We can transport",carpool_capacity,"people today.")

print ("we have",passengers,"to carpool today.")

print ("We need to put about",average_passengers_per_car,"in each car.hahaha")

print ("数学是一切科学的源头和归宿，Turtules乌龟程序“”")