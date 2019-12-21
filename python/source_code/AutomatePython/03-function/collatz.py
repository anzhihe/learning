def collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    print(number)
    return number

try:
    number = int(input("Input a positive integer: "))
    while number != 1:
        number = collatz(number)
except ValueError:
    print("You should input a positive integer.")
