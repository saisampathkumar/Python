# A program to perform Arthematic operations

print("Welcome to ICP 1")
num1 = int(input('Please enter integer 1: '))
num2 = int(input('Please enter integer 2: '))
print("""please enter the option to perform an operation:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. All together
    6. Exit""")
while True:
    inp = int(input("  "))
    if inp == 1:
        print("Addition of %d and %d is %d"%(num1, num2, num1+num2))
    elif inp == 2:
        print("Subtraction of %d and %d is %d"%(num1, num2, num1-num2))
    elif inp == 3:
        print("Multiplication of %d and %d is %d"%(num1, num2, num1*num2))
    elif inp == 4:
        print("Division of %d and %d is %d"%(num1, num2, num1/num2))
    elif inp == 5:
        print("Addition of %d and %d is %d" % (num1, num2, num1 + num2))
        print("Subtraction of %d and %d is %d"%(num1, num2, num1-num2))
        print("Multiplication of %d and %d is %d" % (num1, num2, num1 * num2))
        print("Division of %d and %d is %d" % (num1, num2, (num1 / num2)))
    elif inp == 6:
        break
