import numpy

import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import re

l_model = load_model('my_model.h5')

print(l_model.summary())

new_text = [['A lot of good things are happening. We are respected again throughout the world, and thats a great thing']]
max_df = pd.DataFrame(new_text, index=range(0, 1, 1), columns=list('t'))
max_df['t'] = max_df['t'].apply(lambda x: x.lower())
max_df['t'] = max_df['t'].apply((lambda x: re.sub('[^a-zA-z0-9\s]', '', x)))
max_fatures = 2000
tokenizer = Tokenizer(num_words=max_fatures, split=' ')
tokenizer.fit_on_texts(max_df['t'].values)
X = tokenizer.texts_to_sequences(max_df['t'].values)
X = pad_sequences(X, maxlen=28)

O = l_model.predict(X)
print(O)
print(numpy.where(max(O[0])),":",(max(O[0])))
print(numpy.argmax(O))