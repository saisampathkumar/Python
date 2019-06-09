# A program to reverse a string

while True:
    Str1 = str(input("Please enter a string: "))
    if Str1 != '':
        res = Str1[:1:-1]  # deleting the last two letters after reversing the string
        print(res)
        break
    else:
        print("A string can not be null")
