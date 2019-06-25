import requests
from bs4 import BeautifulSoup
import nltk
import re


wiki = "https://en.wikipedia.org/wiki/Google"
page = requests.get(wiki).text
soup = BeautifulSoup(page,"html.parser")
text = str(soup.encode("UTF-8"))
file = open("input.txt", "w")
file.write(text)
file.close()
nltk.download('punkt')

print('\n Tokenization \n')
'''for s in sTokens:'''
for k in text.split("\n"):
    text1 = str(re.sub(r"[^a-zA-Z0-9]+", ' ', k))
    file = open("input1.txt", "w")
    file.write(text1)

sTokens = nltk.word_tokenize(text1)
for s in sTokens:
    print(s)
