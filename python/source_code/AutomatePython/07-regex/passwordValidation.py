import re

def passwordValidation(pwd):
    if(len(pwd) < 8):
        return False
    upperRegex = re.compile(r'[A-Z]')
    lowerRegex = re.compile(r'[a-z]')
    numberRegex = re.compile(r'[0-9]')

    if upperRegex.search(pwd) and lowerRegex.search(pwd) and numberRegex.search(pwd):
        return True
    else:
        return False

def printResult(pwd):
    print(pwd.ljust(20), passwordValidation(pwd)) 


printResult('HelloWorld123')
printResult('HelloWorld')
printResult('Hello123')
printResult('H')
printResult('elloorld123')
printResult('HW123')