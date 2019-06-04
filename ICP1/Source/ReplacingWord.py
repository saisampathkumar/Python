# A program to replace a word in a provide string

while True:
    Str1 = str(input("Please enter a string: "))
    if Str1 != '':
        while True:
            Str2 = str(input("Please enter the word which have to be replaced:"))
            if Str1.find(Str2) != -1:
                print("The resultant string:", Str1.replace(Str2, Str2 + 's'))
                break
            else:
                print('"' + Str2 + '"', " is not found in the provided string")
        break
    else:
        print("A string can not be be null")
