# A program to convert given string into alternative string

Str = str(input("Enter any string to get an alternative string"))


def String_Alternative(Str):
    # defining a function 
    Str = Str[::2]
    # Converting the input string into alternative string
    print(Str)


String_Alternative(Str)
# Calling the function
