# A program to count the word from a text file
import json

file1 = open("InputFile.txt")
# opening the file
Str1 = file1.readlines()
# reading each line and saving them as an array
Str2 = " "
for N in Str1:
    Str2 += N
# merging each sring in array
str3 = " "

def word_count(str):  # defining a word counter function
    counts = dict()  # assigning a duplicate dictionary using dict function
    words = str.split()  # splitting each words in the string
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts  # returns the updated counter which is of dictionary type

res = word_count(Str2)  # calling the word counter function
print(res)  # printing the resultant count of the words
res = json.dumps(res)   # converting dictionary object into string to save in the file
for i in res:
    str3 += res
# merging each string in the array
file2 = open("InputFile.txt", "a")
# opening the same input file to append the resultant data
file2.write(str3)
# writing the resultant data
print(file2)
