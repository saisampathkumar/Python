import numpy as np
from colorama import Fore
from colorama import Style
x = np.random.randint(1, 20, size=15)
# Assigning 15 random numbers between 1 to 20
print(f"{Fore.GREEN } Original vector: {Style.RESET_ALL} ", x)

y = np.max(x)
# Finding the max value from the initial array
x[np.where(x == y)] = 0
# Replacing the max value with 0
print(f"{Fore.GREEN} Maximum value is: {Style.RESET_ALL} %d  " % y)
print(f"{Fore.GREEN} After Replacing: {Style.RESET_ALL}", x)
