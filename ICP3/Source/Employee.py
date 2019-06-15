import random
from colorama import Fore
from colorama import Style


class Employee:
    # Defining the Parent or Base Class
    EmpCount = 0
    EmpTotalSal = 0

    EmpSal = 0
    EmpFirstName = ""
    EmpLastName = ""
    EmpDep = ""
    EmpEmail = ""
    EmpCntct = 0

    def __init__(self, FirstName, LastName, Dep, Email, Sal, Cntct):
        # Defining the Base class constructor
        self.EmpFirstName = FirstName
        self.EmpLastName = LastName
        self.EmpDep = Dep
        self.EmpEmail = Email
        self.EmpSal = Sal
        self.EmpCntct = Cntct
        Employee.EmpCount += 1
        Employee.EmpTotalSal += Sal


class FullTimeEmployee(Employee):
    # Defining the Child or Derived Class
    EmpId = 0

    def __init__(self, FirstName, LastName, Dep, Email, Sal, Cntct):
        # Defining Derived Class the constructor
        Employee.__init__(self, FirstName, LastName, Dep, Email, Sal, Cntct)
        # Assigning the input to the variable in Base Class
        self.EmpId = int(random.random() * 100000000)
        # Assigning a random ID to the employee Id

    def getEmpDetails(self):
        # Defining a function to print details of an employee
        print(f" Employee Id: {Fore.BLUE + Style.BRIGHT} %d {Style.RESET_ALL} \n"
              f" First Name: {Fore.BLUE + Style.BRIGHT} %s {Style.RESET_ALL} \n"
              f" Last Name: {Fore.BLUE + Style.BRIGHT} %s {Style.RESET_ALL} \n"
              f" Department: {Fore.BLUE + Style.BRIGHT} %s {Style.RESET_ALL} \n"
              f" Email: {Fore.BLUE + Style.BRIGHT} %s {Style.RESET_ALL} \n"
              f" Salary: {Fore.BLUE + Style.BRIGHT} %s {Style.RESET_ALL} \n"
              f" Phone: {Fore.BLUE + Style.BRIGHT} %s {Style.RESET_ALL} \n"
              f"" % (
                  self.EmpId, self.EmpFirstName, self.EmpLastName, self.EmpDep, self.EmpEmail, self.EmpSal,
                  self.EmpCntct))

    def getaverageSal(self):
        # Defining a function to calculate the average salary of all the employee
        avgSal = self.EmpTotalSal / self.EmpCount
        print(f"Avereage salary of all employees: {Fore.RED + Style.BRIGHT}%d{Style.RESET_ALL}" % (avgSal))
        print(f"Total Number of employees: {Fore.RED + Style.BRIGHT}%d{Style.RESET_ALL}" % (self.EmpCount))


print(f"Employee Class Output {Fore.CYAN + Style.DIM}(Parent Class){Style.RESET_ALL}:")
emp1 = Employee("Sampath", "Raigri", "Development", "sai@gmail.com", 20000, 7893771890)
# Creating first employee instance by assigning values
emp2 = Employee("Kiran", "kura", "Testing", "kura@gmail.com ", 15000, 9014136052)
# Creating second employee instance by assigning values
print(f"Employee 1: {Fore.GREEN + Style.BRIGHT}%s %s{Style.RESET_ALL}" % (emp1.EmpFirstName, emp1.EmpLastName))
# Printing details of first employee by calling the members of the Base class using Instance variable
print(f"Employee 2: {Fore.GREEN + Style.BRIGHT}%s %s{Style.RESET_ALL}" % (emp2.EmpFirstName, emp2.EmpLastName), "\n")
# Printing details of first employee by calling the members of the Base class using Instance variable


print(f"Full time Employee Class Output {Fore.CYAN + Style.DIM}(Child Class){Style.RESET_ALL}: ")
emp3 = FullTimeEmployee("ram", "Vag", "Development", "ram@gmail.com", 7000, 9866898933)
# Creating third employee instance by assigning values
print("Full time Employee 3 Details: \n")
emp3.getEmpDetails()
# calling the functions defined in the Derived class using instance variable
emp3.getaverageSal()
