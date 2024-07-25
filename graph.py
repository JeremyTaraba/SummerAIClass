from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pandas
from sklearn.preprocessing import LabelEncoder

# Store the Iris data from Iris.csv into a python dataframe.
df = pandas.read_csv("cereal.csv")
X = df[['calories', 'protein', 'fat','sodium','fiber','carbo','sugars','potass','vitamins','shelf','weight','cups','rating']]

# Insert the species into a dataframe named y.
y = df['name']
print(y)

# Label Encoding to turn values into numerical.
le = LabelEncoder()
yEncoded = le.fit_transform(y)
print(yEncoded)

# we will create a scatter plot.
plt.scatter(X['rating'],X['sugars'],  c = yEncoded, cmap = 'gist_rainbow')
plt.xlabel("Rating", fontsize =18)
plt.ylabel("Sugars", fontsize = 18)
plt.savefig("cereal_plot.png")

km = KMeans(n_clusters = 3, random_state = 0)

km.fit(X)

new_labels = km.labels_
plt.scatter(X['rating'],X['sugars'], c = new_labels, cmap = 'gist_rainbow')
plt.xlabel('Rating', fontsize = 18)
plt.ylabel('Sugars', fontsize = 18)
plt.title("Predicted", fontsize = 18)
plt.savefig("cereal_Prediction.png")