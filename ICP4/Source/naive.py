import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv('./glass.csv')
# Reading the csv file and saving the data into a variable
y = df["Type"]
# saving the column named only 'type' into variable y
df1 = df.drop("Type",axis=1).copy()
# dropping the column named 'type' and saving the remaining data into another variable
X_train, X_test, Y_train, Y_test = train_test_split(df1, y,test_size=0.15)
# create training and testing

model = GaussianNB()
model.fit(X_train,Y_train)
# training the model by providing the test and train data
Y_pred = model.predict(X_test)
# predicting the test accuracy
acc_svc = round(model.score(X_test, Y_test) * 100, 2)
# rounding the resultant score upto two digits after decimal
print("Naive Byes accuracy with test is:", acc_svc)
# printing the accuracy when trained with the svm model