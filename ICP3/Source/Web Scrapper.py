import requests
from colorama import Fore
from colorama import Style
from bs4 import BeautifulSoup
# BS4 is a parsing library to extract data from HTMl or XML page

wiki = "https://en.wikipedia.org/wiki/Deep_learning"
page = requests.get(wiki).text
# requesting the html page of the given wiki link and converting into text format
soup = BeautifulSoup(page, 'html.parser')
# defining the requested page as HTMl page

title = soup.find('title')
# finding the title tag to get the title name using inbuilt find function
print(f"Title: {Fore.CYAN + Style.BRIGHT} %s {Style.RESET_ALL}" %(title.get_text()))
print("::::::::::::::::::::::::::::::::::::::::::::::::")

a = soup.find_all('a')
# finding all the anchor tags and saving them in a variable in array format
for i in a:
    print(f"Anchor Tag: {Fore.GREEN + Style.BRIGHT} %s {Style.RESET_ALL}" %(i.get_text()))
    print(f"href: {Fore.BLUE} %s {Style.RESET_ALL}" %(i.get('href')))
    print("::::::::::::::::::::::::::::::::::::::::::::::::")