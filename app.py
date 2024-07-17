from flask import Flask, jsonify
from flask_cors import CORS
from sklearn import svm  

app = Flask(__name__)
CORS(app)

input_data = [[1,2,3], [4,5,6], [7,8,9]]
output_data = [4,7,10]

model = svm.SVC()
model.fit(input_data, output_data)


@app.route('/predict/<n1>/<n2>/<n3>', methods=['GET'])
def predict(n1,n2,n3):
    message = "The predicted number is " + str(model.predict([[n1,n2,n3]])[0])
    return jsonify(message)

@app.route('/test/<message>', methods=['GET'])
def test_message(message):
    print(message)
    return jsonify(message)

if __name__ == '__main__':
    app.run(host="0.0.0.0")