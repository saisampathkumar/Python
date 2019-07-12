from keras.models import Sequential
from keras import layers
from keras.preprocessing.text import Tokenizer
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.layers.embeddings import Embedding
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Flatten
import matplotlib.pyplot as plt

df = pd.read_csv('imdb_master_new.csv', encoding='latin-1')
print(df.head())
sentences = df['review'].values
y = df['label'].values

# tokenizing data
tokenizer = Tokenizer(num_words=2000)
tokenizer.fit_on_texts(sentences)
# getting the vocabulary of data
# sentences = tokenizer.texts_to_matrix(sentences)

max_review_len = max([len(s.split()) for s in sentences])
vocab_size = len(tokenizer.word_index) + 1
sentences = tokenizer.texts_to_sequences(sentences)
padded_docs = pad_sequences(sentences, maxlen=max_review_len)

le = preprocessing.LabelEncoder()
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(padded_docs, y, test_size=0.25, random_state=1000)

# Number of features
# print(input_dim)
input_dim = 2000
model = Sequential()

model.add(Embedding(vocab_size, 100, input_length=max_review_len))
model.add(Flatten())
model.add(layers.Dense(400, activation='relu'))
model.add(layers.Dense(100, activation='relu'))
model.add(layers.Dense(3, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['acc'])
history = model.fit(X_train, y_train, epochs=2, verbose=True, validation_data=(X_test, y_test), batch_size=256)

# summarize history for accuracy
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

[test_loss, test_acc] = model.evaluate(X_test, y_test)
print("Evaluation result on Test Data : "
      "Loss = {}, "
      "accuracy = {}".format(test_loss, test_acc))
