import pandas as pd
import matplotlib.pyplot as plt


import warnings
warnings.filterwarnings("ignore")

dataset = pd.read_csv('CC.csv')
x = dataset.iloc[:, 1:-1]
y = dataset.iloc[:, -1]
print(x.shape, y.shape)
# see how many samples we have of each species
print(dataset["TENURE"].value_counts())

# Null values
nulls = pd.DataFrame(x.isnull().sum().sort_values(ascending=False)[:])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

print("\n", x.mean())

##handling missing value
data = x.fillna(x.mean())
data.to_csv('Modifiend_CC.csv', index=False)

nulls = pd.DataFrame(data.isnull().sum().sort_values(ascending=False)[:])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
scaler.fit(data)
X_scaled_array = scaler.transform(data)
X_scaled = pd.DataFrame(X_scaled_array, columns=data.columns)

from sklearn.cluster import KMeans
nclusters = 3  # this is the k in kmeans
km = KMeans(n_clusters=nclusters)
km.fit(data)
# predict the cluster for each data point
y_cluster_kmeans = km.predict(data)

from sklearn import metrics
score = metrics.silhouette_score(data, y_cluster_kmeans)
print("\n Silhouette score:",score)

##elbow method to know the number of clusters
wcss = []
for i in range(1, 7):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 7), wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()


from sklearn.decomposition import PCA
#Make an instance of the Model
pca= PCA(2)
X_pca= pca.fit_transform(X_scaled)
print("\n PCA(2) Length:",len(X_pca))
print("\n PCA(2):")
for n in X_pca[:5]:
    print(n)


km.fit(X_pca)
# predict the cluster for each data point
y_cluster_kmeans = km.predict(X_pca)
from sklearn import metrics
score = metrics.silhouette_score(X_pca, y_cluster_kmeans)
print("\n Silhouette score for 2 features:",score)

pca= PCA(3)
X_pca= pca.fit_transform(X_scaled)
print("\n PCA(3) Length:",len(X_pca))
print("\n PCA(3):")
for n in X_pca[:5]:
    print(n)


km.fit(X_pca)
# predict the cluster for each data point
y_cluster_kmeans = km.predict(X_pca)
from sklearn import metrics
score = metrics.silhouette_score(X_pca, y_cluster_kmeans)
print("\n Silhouette score for 3 features:",score)




