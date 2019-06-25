import nltk

file = open("input1.txt", "r")
text1 = file.read()

stokens = nltk.sent_tokenize(text1)
wtokens = nltk.word_tokenize(text1)

nltk.download('averaged_perceptron_tagger')
print('\n Parts of speech \n')
print(nltk.pos_tag(wtokens));
print("\nSTEMMING\n")
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer


pStemmer = PorterStemmer()
lStemmer = LancasterStemmer()
sStemmer = SnowballStemmer('english')

for w in wtokens[:50]:
    print(pStemmer.stem(w),
          lStemmer.stem(w),
          sStemmer.stem(w))





# Lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print("\nLEMMATIZATION\n")
for t in wtokens[:50]:
    print("Lemmatizer:", lemmatizer.lemmatize(t), ",    With POS=n:", lemmatizer.lemmatize(t, pos="n"))





print("\n Trigram \n")
# Trigram
from nltk.util import ngrams
token = nltk.word_tokenize(text1)

for s in stokens[:50]:
     token = nltk.word_tokenize(s)
     bigrams = list(ngrams(token, 2))
     trigrams = list(ngrams(token, 3))
     print("The text:", s, "\nword_tokenize:", token, "\nbigrams:", bigrams, "\ntrigrams", trigrams)




print("\n Named Entity Recognition \n")
from nltk import word_tokenize, pos_tag, ne_chunk

for s in stokens[:50]:
    print(ne_chunk(pos_tag(word_tokenize(s))))
Lstemmer = LancasterStemmer()
sStemmer = SnowballStemmer()
