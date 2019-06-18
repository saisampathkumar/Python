import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

train = pd.read_csv('winequality-red.csv')

print(train.quality.describe())

# Next, we'll check for skewness
print("\nSkew is:", train.quality.skew())

target = np.log(train.quality)
print("\nSkew is:", target.skew())

# Working with Numeric Features
numeric_features = train.select_dtypes(include=[np.number])
corr = numeric_features.corr()
print(corr['quality'].sort_values(ascending=False)[:5], '\n')
print(corr['quality'].sort_values(ascending=False)[-5:])

##Null values
nulls = pd.DataFrame(train.isnull().sum().sort_values(ascending=False)[:])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)



##handling missing value
data = train.select_dtypes(include=[np.number]).interpolate().dropna()
# print((data.isnull().sum() != 0))

nulls = pd.DataFrame(data.isnull().sum().sort_values(ascending=False)[:])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

data.to_csv('Modifiend_winequality_red.csv',index=False)

##Build a linear model
y = np.log(data.quality)
X = data.drop(['quality'], axis=1)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.33)
from sklearn import linear_model
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)

##Evaluate the performance and visualize results
print("R^2 is: \n", model.score(X_test, y_test))
predictions = model.predict(X_test)
from sklearn.metrics import mean_squared_error
print('RMSE is: \n', mean_squared_error(y_test, predictions))
