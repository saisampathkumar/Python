# A program to convert weights in Lbs of N Students into kilograms

list1 = []  # input list
list2 = []  # output list
num = int(input("Enter How many number of students"))

for N in range(0, num):
    val = int(input("Enter the weight value of Student "))
    # getting the value from the user
    list1.append(val)
    # appending values to input list


for i in list1:
    res = (i * 0.453592)
    # calculating each student weight in kilograms
    list2.append(res)
    # appending values in output list

print("Input List:", list1)
# printing input list
print("Required output list", list2)
# printing output list