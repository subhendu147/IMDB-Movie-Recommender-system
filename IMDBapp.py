

from flask import Flask, request, jsonify
import pickle


app = Flask(__name__)


with open('movies.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/predict', methods=['POST'])
def predict():
    
    data = request.json
    
    
    prediction = model.predict(data)
    
    
    return jsonify({'prediction': prediction.tolist()})


if __name__ == '__main__':
    app.run(debug=True)