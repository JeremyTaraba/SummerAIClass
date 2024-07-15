from sklearn import svm
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("Iris.csv")

X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
Y = df[['Species']]


le = LabelEncoder()
yEncoded = le.fit_transform(Y['Species'])

IrisPredictionModel = svm.SVC()

IrisPredictionModel.fit(X.values, yEncoded)

unknown_flower = [[4.9, 3, 1.4, .2]]
prediction = IrisPredictionModel.predict(unknown_flower)

name = le.inverse_transform(prediction)
print(prediction, name)

