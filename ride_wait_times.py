from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
# day, time
day_and_time = [
  [1, 9],
  [1, 10],
  [1, 11],
  [1, 12],
  [1, 13],
  [1, 14],
  [1, 15],
  [1, 16],
  [2, 9],
  [2, 10],
  [2, 11],
  [2, 12],
  [2, 13],
  [2, 14],
  [2, 15],
  [2, 16],
]

# wait times for the day, time
wait_time = [0,10,20,30,40,30,20,10,0,20,40,60,80,60,40,20]

# model = linear_model.LinearRegression()
model = make_pipeline(PolynomialFeatures(2), Ridge()) 
model.fit(day_and_time, wait_time)
print(model.predict([[3,12]]))