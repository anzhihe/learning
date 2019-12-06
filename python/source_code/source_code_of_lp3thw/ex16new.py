from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

# Truncating is not needed since the file is being opened in 'w' write mode
# which automatically truncates the file. Commenting out the lines below:
# print("Truncating the file. Goodbye!")
# target.truncate()

print("Now I'm going to ask you for three line.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# Reduced 6 lines into 3 using the f string format
target.write(f"{line1}\n")
target.write(f"{line2}\n")
target.write(f"{line3}\n")

# Opens the file in read mode 'r', reads the contents, then prints it out
target = open(filename, 'r')
text_in_file = target.read()
print(f"\n{text_in_file}")

print("And finally, we close it.")
target.close()

# The code come from https://github.com/lotspaih/python3HardWay/blob/master/ex16.py
