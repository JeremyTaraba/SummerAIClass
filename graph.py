from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pandas
from sklearn.preprocessing import LabelEncoder

# Store the Iris data from Iris.csv into a python dataframe.
df = pandas.read_csv("Iris.csv")
X = df[['SepalLengthCm', 'SepalWidthCm']]

# Insert the species into a dataframe named y.
y = df['Species']
print(y)

# Label Encoding to turn values into numerical.
le = LabelEncoder()
yEncoded = le.fit_transform(y)
print(yEncoded)

# we will create a scatter plot.
plt.scatter(X['SepalLengthCm'],X['SepalWidthCm'], c = yEncoded, cmap = 'gist_rainbow')
plt.xlabel("Sepal Length", fontsize =18)
plt.ylabel("Sepal Width", fontsize = 18)
plt.savefig("plot.png")

km = KMeans(n_clusters = 3, random_state = 0)

km.fit(X)

new_labels = km.labels_
plt.scatter(X['SepalLengthCm'],X['SepalWidthCm'], c = new_labels, cmap = 'gist_rainbow')
plt.xlabel('Sepal Length', fontsize = 18)
plt.ylabel('Sepal Width', fontsize = 18)
plt.title("Predicted", fontsize = 18)
plt.savefig("Prediction.png")